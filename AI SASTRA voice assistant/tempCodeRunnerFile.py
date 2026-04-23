import pyttsx3
import os
import platform
import subprocess
import cv2
import shutil
from datetime import datetime
import re
import speech_recognition as sr
import sounddevice as sd
import queue
import time
import tkinter as tk
from tkinter import messagebox, simpledialog
import requests

# ─── Patch SpeechRecognition to use sounddevice instead of PyAudio ────────────
class SoundDeviceMicrophone(sr.AudioSource):
    """Microphone using sounddevice — no PyAudio needed!"""

    def __init__(self, device_index=None, sample_rate=16000, chunk_size=1024):
        self.device_index = device_index
        self.SAMPLE_RATE = sample_rate
        self.CHUNK = chunk_size
        self.SAMPLE_WIDTH = 2          # 16-bit = 2 bytes
        self.stream = None
        self._queue = queue.Queue()

    def __enter__(self):
        self.stream = SoundDeviceMicrophone._SoundDeviceStream(
            device=self.device_index,
            samplerate=self.SAMPLE_RATE,
            blocksize=self.CHUNK,
            q=self._queue,
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.stream:
            self.stream.close()
            self.stream = None

    class _SoundDeviceStream:
        def __init__(self, device, samplerate, blocksize, q):
            self._q = q
            self._stream = sd.RawInputStream(
                device=device,
                samplerate=samplerate,
                blocksize=blocksize,
                dtype='int16',
                channels=1,
                callback=self._callback,
            )
            self._stream.start()

        def _callback(self, indata, frames, time_info, status):
            self._q.put(bytes(indata))

        def read(self, num_bytes):
            data = b""
            while len(data) < num_bytes:
                try:
                    chunk = self._q.get(timeout=1.0)
                except Exception:
                    # timeout or other issue: return what we have so recogniser can handle it
                    break
                data += chunk
            return data

        def close(self):
            self._stream.stop()
            self._stream.close()


# ─── Main Assistant ────────────────────────────────────────────────────────────
class AgniastaAssistant:

    def __init__(self):
        # Text-to-speech
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)

        # Speech recogniser (Google free API)
        self.recognizer = sr.Recognizer()
        self.recognizer.pause_threshold = 0.8   # seconds of silence = end of phrase
        self.recognizer.energy_threshold = 300  # mic sensitivity (lower = more sensitive)
        self.recognizer.dynamic_energy_threshold = True

        self.os_type = platform.system()

        # Try to auto-select working input/output devices (or prompt user)
        try:
            self._auto_select_devices()
        except Exception:
            pass

        # Simple in-memory cache for QA responses
        self._qa_cache = {}
        self._qa_cache_size = 200

        print("=" * 50)
        print("  Agniasta Voice Assistant — ONLINE")
        print("=" * 50)
        self._print_devices()
        self.speak("Hello sir, Agniasta is online and ready to assist you.")

    # ── helpers ──────────────────────────────────────────────────────────────

    def _print_devices(self):
        """Show available microphones so user can pick the right one."""
        try:
            print("\nAvailable microphones:")
            devices = sd.query_devices()
            for i, d in enumerate(devices):
                if d.get('max_input_channels', 0) > 0:
                    print(f"  [{i}] {d['name']}")
            default = sd.query_devices(kind='input')
            print(f"\n  Using default input: [{default.get('index')}] {default.get('name')}\n")
        except Exception as e:
            print(f"Could not list audio devices: {e}")

    def _test_input_device(self, index, samplerate=16000, timeout=0.5):
        try:
            stream = sd.RawInputStream(device=index, samplerate=samplerate,
                                       blocksize=1024, dtype='int16', channels=1)
            stream.start()
            try:
                stream.read(1024)
            except Exception:
                # read may fail if device is busy — consider unavailable
                try:
                    stream.stop()
                except Exception:
                    pass
                try:
                    stream.close()
                except Exception:
                    pass
                return False
            try:
                stream.stop()
            except Exception:
                pass
            try:
                stream.close()
            except Exception:
                pass
            return True
        except Exception:
            return False

    def _test_output_device(self, index, samplerate=16000):
        try:
            stream = sd.RawOutputStream(device=index, samplerate=samplerate,
                                        blocksize=1024, dtype='int16', channels=1)
            stream.start()
            stream.stop()
            stream.close()
            return True
        except Exception:
            return False

    def _auto_select_devices(self):
        """Try to find working input/output devices; if none, show a popup to pick."""
        try:
            # try default devices first
            try:
                default_in = sd.query_devices(kind='input')['index']
            except Exception:
                default_in = None
            try:
                default_out = sd.query_devices(kind='output')['index']
            except Exception:
                default_out = None

            good_in = None
            good_out = None

            if default_in is not None and self._test_input_device(default_in):
                good_in = default_in
            if default_out is not None and self._test_output_device(default_out):
                good_out = default_out

            # search for any working device if defaults failed
            if good_in is None or good_out is None:
                devices = sd.query_devices()
                for i, d in enumerate(devices):
                    if good_in is None and d.get('max_input_channels', 0) > 0:
                        if self._test_input_device(i):
                            good_in = i
                    if good_out is None and d.get('max_output_channels', 0) > 0:
                        if self._test_output_device(i):
                            good_out = i
                    if good_in is not None and good_out is not None:
                        break

            # if still missing, prompt user with a simple popup listing indices
            if good_in is None or good_out is None:
                try:
                    root = tk.Tk()
                    root.withdraw()
                    dev_list = sd.query_devices()
                    lines = []
                    for i, d in enumerate(dev_list):
                        lines.append(f"[{i}] {d['name']} (in:{d.get('max_input_channels',0)} out:{d.get('max_output_channels',0)})")
                    messagebox.showinfo("Select Audio Devices",
                                        "No working input/output device auto-detected.\n\nAvailable devices:\n" + "\n".join(lines))
                    if good_in is None:
                        in_idx = simpledialog.askinteger("Input Device",
                                                         "Enter input device index (number):")
                        if in_idx is not None and self._test_input_device(in_idx):
                            good_in = in_idx
                    if good_out is None:
                        out_idx = simpledialog.askinteger("Output Device",
                                                          "Enter output device index (number):")
                        if out_idx is not None and self._test_output_device(out_idx):
                            good_out = out_idx
                    root.destroy()
                except Exception:
                    # fallback to console selection
                    print("No GUI available — please type device indices.")
                    dev_list = sd.query_devices()
                    for i, d in enumerate(dev_list):
                        print(f"[{i}] {d['name']} (in:{d.get('max_input_channels',0)} out:{d.get('max_output_channels',0)})")
                    if good_in is None:
                        try:
                            in_idx = int(input("Enter input device index: "))
                            if self._test_input_device(in_idx):
                                good_in = in_idx
                        except Exception:
                            pass
                    if good_out is None:
                        try:
                            out_idx = int(input("Enter output device index: "))
                            if self._test_output_device(out_idx):
                                good_out = out_idx
                        except Exception:
                            pass

            # apply selection if found
            if good_in is not None or good_out is not None:
                current = sd.default.device
                if isinstance(current, tuple) or isinstance(current, list):
                    cur_in = current[0]
                    cur_out = current[1]
                else:
                    cur_in = current
                    cur_out = None
                sel_in = good_in if good_in is not None else cur_in
                sel_out = good_out if good_out is not None else cur_out
                try:
                    if sel_out is not None:
                        sd.default.device = (sel_in, sel_out)
                    else:
                        sd.default.device = sel_in
                except Exception:
                    try:
                        sd.default.device = sel_in
                    except Exception:
                        pass

        except Exception as e:
            print(f"Device auto-selection error: {e}")

    def ask_question(self, question):
        """Ask an external QA API (OpenAI-compatible by default) and return the answer.

        Configuration via environment:
        - DEEPSEEK_API_URL: optional custom endpoint (defaults to OpenAI chat completions)
        - DEEPSEEK_API_KEY or OPENAI_API_KEY: API key for Authorization
        """
        qkey = (question or '').strip()
        if not qkey:
            return "I didn't get a question."

        # check cache
        cache_key = qkey.lower()
        if cache_key in self._qa_cache:
            return self._qa_cache[cache_key]

        api_url = os.environ.get('DEEPSEEK_API_URL') or 'https://api.openai.com/v1/chat/completions'
        api_key = os.environ.get('DEEPSEEK_API_KEY') or os.environ.get('OPENAI_API_KEY')
        if not api_key:
            self.speak('No API key found for QA service. Set DEEPSEEK_API_KEY or OPENAI_API_KEY.')
            return "(no API key)"

        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        try:
            if 'openai.com' in api_url:
                payload = {
                    'model': 'gpt-3.5-turbo',
                    'messages': [{'role': 'user', 'content': qkey}],
                    'max_tokens': 512,
                    'temperature': 0.2,
                }
                resp = requests.post(api_url, headers=headers, json=payload, timeout=15)
                resp.raise_for_status()
                j = resp.json()
                # safety check for structure
                answer = None
                if isinstance(j, dict):
                    choices = j.get('choices') or []
                    if choices and isinstance(choices, list):
                        answer = choices[0].get('message', {}).get('content')
                if not answer:
                    # fallback to text field
                    answer = j.get('text') or '(no answer)'
            else:
                # Generic endpoint: send question as JSON {"question": "..."}
                payload = {'question': qkey}
                resp = requests.post(api_url, headers=headers, json=payload, timeout=15)
                resp.raise_for_status()
                j = resp.json()
                # try to extract common fields
                answer = j.get('answer') or j.get('text') or str(j)

        except requests.RequestException as e:
            self.speak('Failed to contact QA service. Check your internet or API settings.')
            print(f'QA request error: {e}')
            return '(QA service error)'
        except Exception as e:
            print(f'QA processing error: {e}')
            return '(QA processing error)'

        # cache result
        try:
            if len(self._qa_cache) >= self._qa_cache_size:
                # simple FIFO eviction
                first = next(iter(self._qa_cache))
                del self._qa_cache[first]
            self._qa_cache[cache_key] = answer
        except Exception:
            pass

        return answer

    def speak(self, text):
        print(f"\nAgniasta: {text}")
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            # If TTS fails, fall back to printing the message
            print(f"TTS error: {e}")

    def speak_and_print(self, text):
        """Unified method to speak and print; safe to call anywhere."""
        try:
            self.speak(text)
        except Exception:
            try:
                print(text)
            except Exception:
                pass

    # ── listen ───────────────────────────────────────────────────────────────

    def listen(self):
        """Capture voice via sounddevice, recognise with Google."""
        print("\n🎤  Listening… (speak now)")
        try:
            with SoundDeviceMicrophone() as source:
                # Calibrate for ambient noise (0.5 s)
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                try:
                    audio = self.recognizer.listen(source, timeout=6, phrase_time_limit=10)
                except sr.WaitTimeoutError:
                    print("  (no speech detected — try again)")
                    return ""

            # Recognise
            try:
                command = self.recognizer.recognize_google(audio)
                print(f"  You said: {command}")
                return command.lower()
            except sr.UnknownValueError:
                self.speak("Sorry, I didn't catch that. Could you repeat?")
            except sr.RequestError:
                self.speak("Speech service unreachable. Check your internet connection.")

        except Exception as e:
            print(f"  ⚠ Microphone error: {e}")
            self.speak("I had trouble accessing the microphone.")

        return ""

    # ── open app ─────────────────────────────────────────────────────────────

    def open_application(self, app_name):
        app_name = (app_name or '').strip()
        if not app_name:
            self.speak("No application name provided.")
            return
        self.speak(f"Opening {app_name}")
        try:
            if self.os_type == "Windows":
                apps = {
                    'notepad':     'notepad.exe',
                    'calculator':  'calc.exe',
                    'paint':       'mspaint.exe',
                    'chrome':      'chrome.exe',
                    'firefox':     'firefox.exe',
                    'edge':        'msedge.exe',
                    'explorer':    'explorer.exe',
                    'word':        'winword.exe',
                    'excel':       'excel.exe',
                    'powerpoint':  'powerpnt.exe',
                }
                key = app_name.lower()
                exe = apps.get(key)
                if exe:
                    try:
                        os.startfile(exe)
                    except Exception:
                        subprocess.Popen([exe])
                else:
                    # try to find on PATH
                    found = shutil.which(app_name)
                    if found:
                        subprocess.Popen([found])
                    else:
                        os.system(f'start {app_name}')

            elif self.os_type == "Linux":
                apps = {
                    'firefox':     'firefox',
                    'chrome':      'google-chrome',
                    'calculator':  'gnome-calculator',
                    'terminal':    'gnome-terminal',
                    'files':       'nautilus',
                    'text editor': 'gedit',
                }
                key = app_name.lower()
                cmd = apps.get(key, app_name)
                if shutil.which(cmd):
                    subprocess.Popen([cmd])
                else:
                    subprocess.Popen(cmd, shell=True)

            elif self.os_type == "Darwin":
                apps = {
                    'safari':      'Safari',
                    'chrome':      'Google Chrome',
                    'calculator':  'Calculator',
                    'notes':       'Notes',
                    'terminal':    'Terminal',
                }
                key = app_name.lower()
                app = apps.get(key, app_name)
                subprocess.run(['open', '-a', app])

            self.speak(f"{app_name} opened successfully")

        except Exception as e:
            self.speak(f"Sorry, I couldn't open {app_name}")
            print(f"  Error: {e}")

    # ── camera ───────────────────────────────────────────────────────────────

    def take_photo(self):
        self.speak("Get ready — taking a photo in 3 seconds")
        camera = None
        try:
            camera = cv2.VideoCapture(0)
            if not camera.isOpened():
                self.speak("Sorry, I couldn't access the camera.")
                return

            for i in range(3, 0, -1):
                print(f"  {i}...")
                time.sleep(1)
                camera.read()          # keep buffer fresh

            ret, frame = camera.read()

            if ret:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"photo_{timestamp}.jpg"
                cv2.imwrite(filename, frame)
                self.speak(f"Photo saved as {filename}")
                print(f"  Saved: {os.path.abspath(filename)}")
            else:
                self.speak("Failed to capture photo.")

        except Exception as e:
            self.speak("Camera error occurred.")
            print(f"  Error: {e}")
        finally:
            try:
                if camera is not None:
                    camera.release()
            except Exception:
                pass
            try:
                cv2.destroyAllWindows()
            except Exception:
                pass

    # ── calculate ────────────────────────────────────────────────────────────

    def calculate(self, expression):
        try:
            expression = (expression
                          .replace("plus",          "+")
                          .replace("minus",         "-")
                          .replace("times",         "*")
                          .replace("multiplied by", "*")
                          .replace("divided by",    "/")
                          .replace("x",             "*")
                          .replace("÷",             "/"))
            cleaned = re.sub(r'[^0-9+\-*/().\s]', '', expression).strip()
            if not cleaned:
                raise ValueError("Empty expression")
            try:
                result = eval(cleaned, {"__builtins__": None}, {})
            except ZeroDivisionError:
                self.speak("Error: division by zero.")
                return
            self.speak(f"The answer is {result}")
            print(f"  {cleaned} = {result}")
        except Exception as e:
            self.speak("Sorry, I couldn't calculate that.")
            print(f"  Error: {e}")

    # ── command router ───────────────────────────────────────────────────────

    def process_command(self, command):
        if not command:
            return True

        if isinstance(command, str):
            command = command.lower().strip()
        else:
            return True

        if any(w in command for w in ['exit', 'quit', 'goodbye', 'bye', 'stop']):
            self.speak("Goodbye sir. Have a great day!")
            return False

        elif 'open' in command:
            app = command.replace('open', '').strip()
            self.open_application(app)

        elif any(p in command for p in ['take photo', 'take picture', 'click photo',
                                         'capture photo', 'take a photo']):
            self.take_photo()

        elif any(w in command for w in ['calculate', 'what is', 'compute', 'solve']):
            expr = command
            for w in ['calculate', 'what is', 'compute', 'solve', 'agniasta']:
                expr = expr.replace(w, '')
            self.calculate(expr.strip())

        elif command.startswith('ask ') or command.startswith('question ') or command.startswith('askme '):
            # get the question text after the keyword
            q = command.split(' ', 1)[1].strip() if ' ' in command else ''
            if not q:
                self.speak('Please tell me the question after asking. For example: ask what is photosynthesis')
            else:
                answer = self.ask_question(q)
                if answer:
                    # speak and print the answer
                    try:
                        self.speak_and_print(answer)
                    except Exception:
                        print(answer)

        elif 'time' in command:
            self.speak(f"The time is {datetime.now().strftime('%I:%M %p')}")

        elif 'date' in command:
            self.speak(f"Today is {datetime.now().strftime('%B %d, %Y')}")

        elif 'help' in command or 'what can you do' in command:
            self.speak("Here is what I can do:")
            self.speak("Say open, then an app name — to launch any application.")
            self.speak("Say take photo — to capture a picture from your camera.")
            self.speak("Say calculate, then a math problem — for calculations.")
            self.speak("Say time or date — for the current time or date.")
            self.speak("Say exit or goodbye — to shut me down.")

        else:
            self.speak("I'm not sure about that. Say help to hear what I can do.")

        return True

    # ── main loop ────────────────────────────────────────────────────────────

    def run(self):
        running = True
        while running:
            try:
                command = self.listen()
                running = self.process_command(command)
            except KeyboardInterrupt:
                try:
                    self.speak("Keyboard interrupt received. Shutting down.")
                except Exception:
                    print("Keyboard interrupt received. Shutting down.")
                break
            except Exception as e:
                # Log and continue loop so single errors don't stop the assistant
                try:
                    self.speak("An error occurred while handling your request. I will continue listening.")
                except Exception:
                    print("An error occurred while handling your request.")
                print(f"Runtime error in main loop: {e}")
                # small delay to avoid tight error loop
                time.sleep(0.5)


# ─── Entry point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    try:
        agniasta = AgniastaAssistant()
        agniasta.run()
    except KeyboardInterrupt:
        print("\n\nAgniasta shutting down. Goodbye!")
    except Exception as e:
        print(f"\nFailed to start Agniasta: {e}")
        print("Run this to install everything:")
        print("pip install SpeechRecognition sounddevice pyttsx3 opencv-python")