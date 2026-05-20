# 🐍 Rudra's Python Playground

[![Python](https://img.shields.io/badge/Python-100%25-blue?style=flat-square&logo=python)](https://github.com/rudra520/Python)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL%203.0-green?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![GitHub Stars](https://img.shields.io/github/stars/rudra520/Python?style=flat-square)](https://github.com/rudra520/Python/stargazers)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--05--15-lightgrey?style=flat-square)](https://github.com/rudra520/Python)

Welcome to my personal collection of **Python experiments**, **automation tools**, and **learning snippets** — from **WhatsApp bulk messaging** to **Cisco network scripting** and **function argument mastery**. 

Whether you're here to steal a useful script or just curious how *positional vs. keyword arguments* work, you're in the right place. 😎

---

## 📑 Table of Contents
- [📂 Repository Structure](#-repository-structure)
- [🔥 Featured Scripts](#-featured-scripts)
- [🛠️ Installation & Setup](#️-installation--setup)
- [💻 Usage Examples](#-usage-examples)
- [📚 Learning Topics](#-learning-topics)
- [📋 Requirements](#-requirements)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [👤 About](#-about)

---

## 📂 Repository Structure

<details>
<summary><b>Click to expand folder tree</b></summary>

```
📦 Python (root)
│
├── 📁 ASSIGNMENTS/
│   ├── Sales Automation.py           # 📧 Auto-generate sales reports & emails
│   └── numconverter.py               # 🔄 Binary ↔ Hex ↔ Decimal converter
│
├── 📁 Project by Rudra/
│   ├── whatappmassagesender.py       # 💬 Send bulk WhatsApp messages
│   ├── Piechart.py                   # 📊 Create pie charts from user input
│   └── QRCODE.py                     # 🔲 Generate QR codes from URLs
│
├── 📁 cisco/                         # 🌐 Cisco Network Automation Scripts
│   ├── 📁 Foundation/
│   │   ├── program01.py              # Loops & Conditionals
│   │   ├── program02.py              # String Operations
│   │   ├── program03.py              # Input/Output
│   │   └── program04.py              # Data Structures
│   │
│   └── 📁 Function/
│       ├── Function-1.py             # Basic Functions
│       ├── Keyword argument passing.py
│       ├── Mixing positional and keyword argument.py
│       ├── Parametrized functions.py
│       ├── positional parameter passing.py
│       ├── positional parameter passing 2.py
│       └── return instruction.py     # Return Statements
│
└── 📄 README.md                      # 👈 You are here

```

</details>

---

## 🔥 Featured Scripts

### 1. **WhatsApp Bulk Messenger** `⭐⭐⭐⭐⭐`
> 📁 `Project by Rudra/whatappmassagesender.py`

Send automated WhatsApp messages to multiple contacts instantly using `PyWhatKit`.

**Use Cases:**
- 📢 Bulk reminders & alerts
- 🎉 Automated festive wishes
- 📲 Notification broadcasts

<details>
<summary>📌 View Code Example</summary>

```python
import pywhatkit

# Send a message to a contact
pywhatkit.sendwhatmsg(
    phone_no="+91XXXXXXXXXX",
    message="Hello! This is an automated message.",
    time_hour=15,
    time_min=30
)
```

</details>

---

### 2. **Pie Chart Generator** `⭐⭐⭐⭐`
> 📁 `Project by Rudra/Piechart.py`

Create beautiful, interactive pie charts directly from user input using **Matplotlib**.

**Features:**
- 🎨 Customizable colors & labels
- 💾 Auto-save as PNG
- 🖱️ Interactive data entry

<details>
<summary>📌 View Usage Example</summary>

```bash
$ python Piechart.py
Enter labels (comma-separated): Sales, Marketing, R&D
Enter values (comma-separated): 500, 300, 200
✅ Chart saved as piechart.png
```

</details>

---

### 3. **QR Code Creator** `⭐⭐⭐⭐`
> 📁 `Project by Rudra/QRCODE.py`

Generate QR codes instantly from any URL using the `qrcode` library.

**Perfect for:**
- 🔗 Sharing links dynamically
- 📡 Wi-Fi configuration codes
- 🆔 Contact card distribution

<details>
<summary>📌 View Usage Example</summary>

```bash
$ python QRCODE.py
Enter URL: https://github.com/rudra520
✅ QR code saved as qrcode.png
```

</details>

---

### 5. **Sales Automation** `⭐⭐⭐`
> 📁 `ASSIGNMENTS/Sales Automation.py`

Auto-generate CSV sales reports and email summaries programmatically.

<details>
<summary>📌 Features</summary>

- 📊 Generate reports in CSV/JSON
- 📧 Email report attachments
- 🔄 Batch processing support

</details>

---

### 6. **Number Converter** `⭐⭐⭐`
> 📁 `ASSIGNMENTS/numconverter.py`

Convert between **binary**, **hexadecimal**, and **decimal** formats.

**Great for:**
- 🐛 Low-level debugging
- 📖 Exam preparation
- 🧮 Learning number systems

---

## 🛠️ Installation & Setup

<details open>
<summary><b>📦 Prerequisites</b></summary>

- Python 3.7+
- pip (Python package manager)

</details>

<details>
<summary><b>🔧 Step 1: Clone the Repository</b></summary>

```bash
git clone https://github.com/rudra520/Python.git
cd Python
```

</details>

<details>
<summary><b>📥 Step 2: Install Dependencies</b></summary>

```bash
# For WhatsApp and Network scripts
pip install pywhatkit matplotlib qrcode pillow netmiko

# Or install individual packages as needed
pip install pywhatkit    # WhatsApp messaging
pip install matplotlib   # Pie charts
pip install qrcode       # QR code generation
pip install pillow       # Image processing
pip install netmiko      # Cisco automation
```

</details>

<details>
<summary><b>✅ Step 3: Verify Installation</b></summary>

```bash
python -c "import pywhatkit, matplotlib, qrcode; print('✅ All dependencies installed!')"
```

</details>

---

## 💻 Usage Examples

<details>
<summary><b>🚀 Run WhatsApp Messenger</b></summary>

```bash
cd "Project by Rudra"
python whatappmassagesender.py
```

**⚠️ Important Notes:**
- Must be logged into WhatsApp Web
- Allow time for QR scan (~5 seconds)
- Browser must remain open

</details>

<details>
<summary><b>📊 Create a Pie Chart</b></summary>

```bash
cd "Project by Rudra"
python Piechart.py
# Follow interactive prompts
```

</details>

<details>
<summary><b>🔲 Generate QR Code</b></summary>

```bash
cd "Project by Rudra"
python QRCODE.py
# Enter URL when prompted
```

</details>

<details>
<summary><b>🌐 Run Cisco Foundation Scripts</b></summary>

```bash
cd cisco/Foundation
python program01.py
```

</details>

---

## 📚 Learning Topics

| Topic | Difficulty | Files | Time |
|-------|-----------|-------|------|
| **Python Basics** | ⭐ Beginner | `cisco/Foundation/` | 1-2 hrs |
| **Function Arguments** | ⭐⭐ Intermediate | `cisco/Function/` | 2-3 hrs |
| **Automation with PyWhatKit** | ⭐⭐ Intermediate | `whatappmassagesender.py` | 1-2 hrs |
| **Data Visualization** | ⭐⭐ Intermediate | `Piechart.py` | 1 hr |
| **Network Automation** | ⭐⭐⭐ Advanced | `cisco/` | 3+ hrs |

---

## 📋 Requirements

<details open>
<summary><b>Dependencies</b></summary>

```
pywhatkit>=5.0        # WhatsApp messaging
matplotlib>=3.5.0     # Pie charts & visualization
qrcode>=7.3           # QR code generation
Pillow>=8.0           # Image processing
netmiko>=4.0          # Cisco device automation
```

</details>

---

## 🌟 Why This Repository Exists

- 📚 **Learn by doing** – Every script was written while mastering Python
- 🤖 **Automate boring stuff** – Sales reports, messages, network configs
- 🧩 **Save snippets** – Argument passing patterns in one place
- 🎓 **Preparation for certifications** – CCNA, Python fundamentals
- 💡 **Share knowledge** – Help others learn automation & networking

---

## 🤝 Contributing

I welcome contributions! Here's how to help:

<details>
<summary><b>📝 Contribution Steps</b></summary>

1. **Fork** the repository
   ```bash
   git clone https://github.com/YOUR-USERNAME/Python.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** & test thoroughly

4. **Commit with a clear message**
   ```bash
   git commit -m "Add: [description of changes]"
   ```

5. **Push and create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

**All skill levels welcome!** 🎉

</details>

---

## 📜 License

<details open>
<summary><b>GNU General Public License v3.0</b></summary>

This project is licensed under the **GPL-3.0 License**.

### You are free to:
- ✅ **Use** the software for any purpose
- ✅ **Study** how the software works
- ✅ **Modify** the software to suit your needs
- ✅ **Distribute** copies of the software
- ✅ **Distribute** modified versions of the software

### Under these conditions:
- 📋 **License and copyright notice** must be included
- 📝 **Source code** must be made available when distributing
- ⚖️ **Same license** must apply to modifications and derivative works
- 🔔 **Changes** must be documented and clearly marked

### You are NOT permitted to:
- ❌ Hold the author liable for any damages
- ❌ Use the software for proprietary/closed-source projects without sharing modifications

**Full License Text:** [https://www.gnu.org/licenses/gpl-3.0.en.html](https://www.gnu.org/licenses/gpl-3.0.en.html)

**Copyright © 2024-2026 Rudra520**

</details>

---

## 👤 About

Hi! I'm **Rudra**, a Python enthusiast passionate about:
- 🐍 Python automation & scripting
- 🌐 Network engineering (Cisco/NetDevOps)
- 📱 Building useful tools
- 📚 Learning & sharing knowledge

### Connect with me:
- 🐙 GitHub: [@rudra520](https://github.com/rudra520)
- 💼 Feel free to fork, star ⭐, and contribute!

---

<div align="center">

**Made with ❤️ and many Stack Overflow tabs by Rudra**

*If you found this repository helpful, please consider giving it a ⭐ star!*

</div>
