
# 🚀 Rudra's Python Playground

Welcome to my personal collection of Python experiments, automation tools, and learning snippets — from **WhatsApp bulk messaging** to **Cisco network scripting** and **function argument mastery**.  
Whether you're here to steal a useful script or just curious how *positional vs. keyword arguments* work, you're in the right place. 😎


## 📂 What's Inside?

```
📦 Root
├── 📁 ASSIGNMENTS
│   ├── Sales Automation.py       # Auto‑generate sales reports / emails
│   ├── numconverter.py           # Binary, hex, decimal conversion tool
│
├── 📁 Project by Rudra
│   ├── whatappmassagesender.py   # Send bulk WhatsApp messages (PyWhatKit)
│   ├── Piechart.py               # Create Piechart by user input (Matplotlib)
│   ├── QRCODE.py                 # Create QR code by givig just url (qrcode)
│  
│ 
├── 📁 cisco                      # Cisco network automation scripts
│     ├── 📁 Foundation
│     │    ├── program01.py ~ program04.py  # Core Python basics (loops, conditions, I/O)
│     │
│     ├── 📁 Function
│          ├── Function-1.py
│          ├── Keyword argument passing.py
│          ├── Mixing positional and keyword argument.py
│          ├── Parametrized functions.py
│          ├── positional parameter passing.py
│          └── positional parameter passing 2.py
│
└── 📄 README.md                   # You are here ✨

```


## 🔥 Featured Scripts

### 1. WhatsApp Bulk Messenger (`whatappmassagesender.py`)
Send automated WhatsApp messages to multiple contacts using `pywhatkit`.  
*Perfect for reminders, festive wishes, or just annoying your friends* 😉

```python
# Quick peek
import pywhatkit
pywhatkit.sendwhatmsg("+91XXXXXX", "Hello from Rudra's bot!", 15, 30)
```

### 2. Sales Automation (`ASSIGNMENTS/Sales Automation.py`)
Generates sales summaries, CSV reports, or email drafts – built for a college assignment, but works for real hustle.

### 3. Cisco Network Toolkit (`Project by Rudra/cisco/`)
SSH config push, VLAN setup, or interface status checker – simplify your CCNA lab work with Python + Netmiko.

### 4. Function Argument Demos (`Function/`)
Learn Python arguments the visual way:
- `positional parameter passing.py` → basics
- `Keyword argument passing.py` → readability wins
- `Mixing positional and keyword .py` → best practices
- `Parametrized functions.py` → default values & flexibility

### 5. Foundation Series (`Foundation/`)
From `program01.py` (hello world) to `program04.py` (loops & lists) – my stepping stones into Python.

---

## 🛠️ How to Run

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install dependencies** (if any)  
   ```bash
   pip install pywhatkit netmiko   # for WhatsApp & Cisco scripts
   ```

3. **Run any script**  
   ```bash
   python "Project by Rudra/whatappmassagesender.py"
   ```

> ⚠️ *WhatsApp script requires you to be logged into WhatsApp Web and may need a short delay for QR scan.*

---

## 📌 Why This Repo Exists

- 📚 **Learn by doing** – every script was written while learning Python.
- 🤖 **Automate boring stuff** – sales, messages, network configs.
- 🧩 **Save snippets** – argument passing patterns are hard to remember; now they're in one place.

---

## 🤝 Contributions

Spotted a bug? Have a cooler WhatsApp automation idea?  
Feel free to **fork**, **open an issue**, or submit a **PR**. All skill levels welcome.

---

## 📜 License

MIT — use it, break it, improve it, and don't forget to star ⭐ if you found something useful!

---

**Made with ☕ and many Stack Overflow tabs by Rudra**  

```
