# ⚡ FREE FIRE TCP BOT — OB54

<p align="center">
  <img src="https://img.shields.io/badge/FREE%20FIRE-OB54-ff6b00?style=for-the-badge&logo=gamepad&logoColor=white" alt="Free Fire OB54">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Protocol-TCP-00A67E?style=for-the-badge" alt="TCP">
  <img src="https://img.shields.io/badge/Status-Active-2ea44f?style=for-the-badge" alt="Status">
</p>

<p align="center">
  <b>🎮 A Python-based TCP bot project for learning, testing, and protocol experimentation.</b>
</p>

<p align="center">
  <a href="https://github.com/HussnainsK/Free-Fire-TCPBOT-OB54">⭐ Repository</a> •
  <a href="https://github.com/HussnainsK/Free-Fire-TCPBOT-OB54/issues">🐛 Issues</a>
</p>

---

## 🏆 About The Project

**Free-Fire-TCPBOT-OB54** is a Python-based TCP bot project containing networking logic, Protocol Buffer modules, configuration/data files, and game-client request handling.

The project is intended for **educational, testing, and research purposes**. It is not affiliated with or endorsed by Garena.

> ⚠️ **Important:** Use this project only with accounts and systems you are authorized to test. Do not use it to abuse, disrupt, or interfere with other players or services.

---

## ✨ Features

- ⚡ TCP/network-based bot functionality
- 🐍 Python implementation
- 🔐 Bearer-token based authenticated requests
- 📦 Protocol Buffer (`Pb2`) modules
- 🔄 Runtime token handling
- 🎯 Player/profile request functionality
- 🎮 Free Fire OB54-oriented protocol data
- 🛠️ Configurable project structure

---

## 📂 Project Structure

```text
Free-Fire-TCPBOT-OB54/
│
├── 📁 Pb2/
│   ├── MajoRLoGinrEq_pb2.py
│   ├── MajoRLoGinrEs_pb2.py
│   ├── DEcwHisPErMsG_pb2.py
│   ├── GenWhisperMsg_pb2.py
│   ├── PorTs_pb2.py
│   ├── Team_msg_pb2.py
│   ├── kyro_title_pb2.py
│   ├── room_join_pb2.py
│   └── sQ_pb2.py
│
├── 📄 app.py
├── 📄 xDL.py
├── 📄 emotes.json
├── 📄 requirements.txt
├── 🔐 token.json
└── 📄 README.md
```

> 🔒 **Security note:** Never commit real credentials, passwords, access tokens, or private session tokens to a public repository. `token.json` should not contain a usable secret in a public release.

---

# 🔐 Authentication Architecture

The project does not use a conventional website-style session login. Its networking code uses **Bearer-token authentication** when communicating with the game-client API.

### 🧩 Main Components

| Component | Purpose |
|---|---|
| `app.py` | Main application/bot logic |
| `xDL.py` | Networking, token handling, request construction |
| `token.json` | Token/metadata storage present in the repository |
| `token.txt` | Runtime token storage used by `xDL.py` |
| `Pb2/MajoRLoGinrEq_pb2.py` | Login-request Protocol Buffer definitions |
| `Pb2/MajoRLoGinrEs_pb2.py` | Login-response Protocol Buffer definitions |
| `Pb2/` | Generated Protocol Buffer message modules |

The repository currently contains login-related protobuf modules and networking code in `xDL.py`. The README previously described Guest UID/password configuration, while the code also uses token-based authorization. 

---

## 🔑 How Credentials & Tokens Are Handled

At a high level, the request code follows this pattern:

```text
┌──────────────────────┐
│ Bot / Python process │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Obtain / read token  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Build encoded packet │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────────────┐
│ Authorization: Bearer <JWT>  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Authenticated game API POST  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Decode / parse response      │
└──────────────────────────────┘
```

`xDL.py` defines `GeTToK()` to read a runtime token from `token.txt`. Its authenticated requests then place that value in an HTTP `Authorization` header using the `Bearer` scheme.

The code also contains a background `ToK()` routine that contacts an external token service, selects a returned token, and writes it to `token.txt` periodically.

> ⚠️ **Never publish the resulting token or a real account credential.** Treat access tokens like passwords: keep them private, rotate exposed credentials, and use environment variables or a proper secret manager for production deployments.

---

# 🔄 Request Flow

A simplified authenticated request looks like this:

```text
User / Bot Command
       │
       ▼
Python Bot Logic
       │
       ▼
Build UID / request payload
       │
       ▼
Encode / encrypt request data
       │
       ▼
Read runtime Bearer token
       │
       ▼
HTTP POST → Game Client API
       │
       ▼
Binary / encoded response
       │
       ▼
Decode response
       │
       ▼
Extract requested data
       │
       ▼
Return result to bot
```

For example, the player-information functions in `xDL.py` construct encoded data and send it to the `GetPlayerPersonalShow` endpoint with a Bearer authorization header.

---

# 📥 Clone Repository

<div align="center">

### 🚀 Get The Project

```bash
git clone https://github.com/HussnainsK/Free-Fire-TCPBOT-OB54.git
cd Free-Fire-TCPBOT-OB54
```

[![Clone Repository](https://img.shields.io/badge/🚀_CLONE_REPOSITORY-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/HussnainsK/Free-Fire-TCPBOT-OB54)

</div>

---

# 🛠️ Installation

### 1️⃣ Install Python

Install a supported Python 3.x release and verify it:

```bash
python --version
```

### 2️⃣ Clone the repository

```bash
git clone https://github.com/HussnainsK/Free-Fire-TCPBOT-OB54.git
cd Free-Fire-TCPBOT-OB54
```

### 3️⃣ Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4️⃣ Configure secrets safely

Do **not** paste real passwords or tokens into source files or commit them to GitHub. Use environment variables or a local, ignored configuration file instead.

Example pattern:

```text
TOKEN=<your-private-token>
UID=<your-authorized-test-account-uid>
```

Add secret/config files to `.gitignore` before committing changes.

---

# 🚀 Running

After installing dependencies and configuring your authorized test environment, start the project using the appropriate Python entry point supplied with your deployment:

```bash
python app.py
```

If your local version uses another entry point, follow the project's current source/configuration rather than guessing a command.

---

# 🔒 Security Checklist

Before publishing or deploying:

- [ ] Remove real tokens from `token.json`.
- [ ] Rotate/revoke any token that has already been exposed publicly.
- [ ] Never publish passwords.
- [ ] Never publish private session credentials.
- [ ] Add secret files to `.gitignore`.
- [ ] Use environment variables or a secret manager.
- [ ] Test only accounts and systems you are authorized to use.

> 🚨 **If a credential has been pushed to GitHub, deleting the file alone is not enough. Rotate/revoke the credential because it may remain in Git history or caches.**

---

# 📜 Disclaimer

This project is provided for **educational and testing purposes only**. The author does not encourage cheating, abuse, unauthorized access, service disruption, or violation of game/platform rules.

**Free Fire** and related trademarks belong to their respective owners. This project is an independent community project and is not affiliated with Garena.

---

# 👨‍💻 Credits

<div align="center">

### ⚡ Hussnain sK

**Developer / Repository Owner**

[![GitHub](https://img.shields.io/badge/GitHub-HussnainsK-181717?style=for-the-badge&logo=github)](https://github.com/HussnainsK)

</div>

---

# ⭐ Support The Project

If this project is useful for your **learning and testing**, consider giving the repository a ⭐ on GitHub.

<p align="center">
  <b>🎮 CODE • TEST • LEARN • BUILD ⚡</b>
</p>
