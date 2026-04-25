
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


```markdown
## 🔥 Featured Scripts (New & Improved)

### 1. WhatsApp Bulk Messenger (`Project by Rudra/whatappmassagesender.py`)
Send automated WhatsApp messages to multiple contacts using `pywhatkit`.  
*Ideal for reminders, bulk alerts, or festive wishes.*

```python
import pywhatkit
pywhatkit.sendwhatmsg("+91XXXXXX", "Hello from Rudra!", 15, 30)
```

### 2. Piechart Generator (`Project by Rudra/Piechart.py`)
Create beautiful pie charts directly from user input using `matplotlib`.  
No data wrangling – just enter labels & values, get a chart.

```bash
python Piechart.py
# Enter sales: 500, marketing: 300, R&D: 200 → boom! 🥧
```

### 3. QR Code Creator (`Project by Rudra/QRCODE.py`)
Generate a QR code instantly from any URL using the `qrcode` library.  
Great for sharing links, Wi-Fi configs, or contact cards.

```python
python QRCODE.py
# Paste your URL → qrcode.png appears in the folder
```

### 4. Cisco Network Automation (`cisco/`)
Scripts to push configs, check interfaces, or automate VLANs – ideal for CCNA/NetDevOps.

- **Foundation scripts** (`cisco/Foundation/program01.py` to `04.py`) – Python basics tailored for networking.
- **Function demos** (`cisco/Function/`) – Master positional, keyword, mixed, and parametrized arguments in Python.

### 5. Sales Automation (`ASSIGNMENTS/Sales Automation.py`)
Auto-generate CSV sales reports or email summaries – built for an assignment but scalable for real use.

### 6. Number Converter (`ASSIGNMENTS/numconverter.py`)
Convert between binary, hex, decimal – perfect for low‑level debugging or exam prep.
```

Would you like me to regenerate the **entire README** with this updated structure and featured section?

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
