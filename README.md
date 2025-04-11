![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)
![Last Commit](https://img.shields.io/github/last-commit/DecryptMike/DecryptMike-Password-Manager)
![License](https://img.shields.io/github/license/DecryptMike/DecryptMike-Password-Manager)
![Made With](https://img.shields.io/badge/Made%20with-Cryptography-green?logo=python)

<p align="center">
  <img src="DecryptMikeLogo.png" alt="DecryptMike Logo" style="max-width: 100%; height: auto;"/>
</p>

<h3 align="center">
  🔐 AES-Encrypted Password Manager
</h3>

<h5 align="center">
   A simple, secure command-line password manager built in Python.<br>Encrypts your credentials using AES (Fernet) and stores them in a local vault.
</h5>

---

## 🛠️ Features

- Add new credentials (site, username, password)
- Secure AES-based encryption (via `cryptography.fernet`)
- View stored passwords (decrypted live)
- JSON vault storage (`vault.json`)
- CLI interface for interaction
- Key security via `vault.key` (ignored by Git)

---

## 📁 Tech Stack & Requirements

- **Python 3.6+**
- `cryptography`
- Command-line interface
- File-based storage (`vault.json`)
- AES 128-bit encryption (Fernet)

To install dependencies, run:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Clone the repo

```bash
git clone https://github.com/DecryptMike/DecryptMike-Password-Manager.git
cd DecryptMike-Password-Manager
```

### 2. Set up virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate your encryption key (run once)

```bash
python generate_key.py
```

### 5. Run the password manager

```bash
python vault.py
```

---

## 🧪 Sample Output

```
🔐 Password Vault
1. Add new entry
2. View saved entries
3. Exit
Select an option: 1
Enter site name: github
Enter username: decryptmike
Enter password: h4ck3rbyt3s
✅ Entry added for github

Select an option: 2

🌐 github
👤 Username: decryptmike
🔑 Password: h4ck3rbyt3s
```

---

## 📄 Why I Built It

To strengthen my cybersecurity foundations and demonstrate real-world encryption handling through Python.  
This vault is designed for educational use and as a base for more advanced features.

---

## ⚠️ Legal Disclaimer

This tool is intended for **educational and authorized personal use only**.  
Do not use it to store sensitive or production passwords without enhancements.

---

## 💻 Built by [@DecryptMike](https://github.com/DecryptMike)

---

<p align="center">
  <img src="https://img.shields.io/badge/Built%20for-Cybersecurity-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Made%20by-DecryptMike-green?style=for-the-badge"/>
</p>