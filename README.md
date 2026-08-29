<div align="center">

# ⚡ FREE FIRE TCP BOT — OB54

### Professional Python TCP Bot Project

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Protocol-TCP-111827?style=flat-square" alt="TCP">
  <img src="https://img.shields.io/badge/Release-OB54-F97316?style=flat-square" alt="OB54">
  <img src="https://img.shields.io/badge/Status-Active-16A34A?style=flat-square" alt="Active">
  <img src="https://img.shields.io/badge/Purpose-Educational-7C3AED?style=flat-square" alt="Educational">
</p>

<p>
  <a href="https://github.com/HussnainsK/Free-Fire-TCPBOT-OB54">Repository</a> •
  <a href="https://github.com/HussnainsK/Free-Fire-TCPBOT-OB54/issues">Issues</a> •
  <a href="https://github.com/HussnainsK/Free-Fire-TCPBOT-OB54/stargazers">Stars</a>
</p>

</div>

---

## 📌 Overview

**Free-Fire-TCPBOT-OB54** is a Python networking project built around TCP-style bot functionality, Protocol Buffers, encoded request payloads, and authenticated HTTP requests.

The repository is primarily intended for **learning, testing, and protocol research** in controlled environments.

> **Disclaimer:** This is an independent community project. It is not affiliated with, sponsored by, or endorsed by Garena or Free Fire.

---

## ✨ Highlights

- **Python-based** implementation
- **TCP/networking** functionality
- **Protocol Buffer** message modules
- **Bearer-token authentication** for authenticated requests
- **Encoded request/response** processing
- **Player/profile** request handling
- **OB54-oriented** protocol data
- Simple, modular project layout

---

## 🧱 Architecture

```text
┌───────────────────────┐
│     Python Bot App    │
│        app.py         │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Networking / Protocol │
│        xDL.py         │
└───────────┬───────────┘
            │
       ┌────┴─────┐
       ▼          ▼
┌────────────┐ ┌──────────────┐
│   Pb2/     │ │ Token Layer  │
│ Protobuf   │ │ Bearer JWT   │
└─────┬──────┘ └──────┬───────┘
      │               │
      └───────┬───────┘
              ▼
      ┌───────────────┐
      │ Game API /    │
      │ Network Layer │
      └───────────────┘
```

---

## 🔐 Authentication

The networking code uses **Bearer-token authentication** for authenticated game-client requests. This is different from a normal website session-based login.

### Authentication components

| Component | Responsibility |
|---|---|
| `app.py` | Main application and bot logic |
| `xDL.py` | Networking, token retrieval, request construction and response processing |
| `Pb2/` | Protocol Buffer message definitions |
| `MajoRLoGinrEq_pb2.py` | Login-request message definitions |
| `MajoRLoGinrEs_pb2.py` | Login-response message definitions |
| `token.txt` | Runtime token storage referenced by the networking code |
| `token.json` | Token/metadata file currently present in the repository |

### Request flow

```text
Bot command
    │
    ▼
Build request payload
    │
    ▼
Encode / encrypt payload
    │
    ▼
Read runtime token
    │
    ▼
Authorization: Bearer <token>
    │
    ▼
HTTP POST request
    │
    ▼
Receive binary / encoded response
    │
    ▼
Decode / parse response
    │
    ▼
Return requested data
```

The current `xDL.py` implementation reads a runtime token from `token.txt` and places it in an HTTP `Authorization` header using the `Bearer` scheme. It also contains a background routine that periodically requests tokens from an external service and writes a selected token to `token.txt`.

> 🔒 **Security:** Never publish passwords, access tokens, session credentials, or other private authentication material. Any credential accidentally committed to a public repository should be revoked/rotated immediately.

---

## 📁 Repository Structure

```text
Free-Fire-TCPBOT-OB54/
│
├── Pb2/
│   ├── DEcwHisPErMsG_pb2.py
│   ├── Fo_pb2.py
│   ├── GenWhisperMsg_pb2.py
│   ├── MajoRLoGinrEq_pb2.py
│   ├── MajoRLoGinrEs_pb2.py
│   ├── PorTs_pb2.py
│   ├── Team_msg_pb2.py
│   ├── kyro_title_pb2.py
│   ├── room_join_pb2.py
│   └── sQ_pb2.py
│
├── app.py
├── xDL.py
├── emotes.json
├── requirements.txt
├── token.json
└── README.md
```

---

## 📥 Installation

### 1. Clone

```bash
git clone https://github.com/HussnainsK/Free-Fire-TCPBOT-OB54.git
cd Free-Fire-TCPBOT-OB54
```

### 2. Verify Python

```bash
python --version
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure secrets safely

Do **not** place real passwords or tokens directly in source code or commit them to GitHub.

For local development, prefer environment variables or an ignored configuration file:

```text
TOKEN=<private-token>
UID=<authorized-test-account-uid>
```

Add local secret files to `.gitignore` before committing changes.

---

## ▶️ Running

After installing dependencies and configuring an authorized test environment:

```bash
python app.py
```

The exact runtime behavior depends on the current source code and deployment environment.

---

## 🛡️ Security Best Practices

- Never publish credentials or session tokens.
- Rotate credentials immediately if they are exposed.
- Do not rely on deleting a secret file alone; exposed values can remain in Git history.
- Keep local secret/configuration files out of version control.
- Use environment variables or a dedicated secret manager for deployments.
- Test only accounts and systems you are authorized to use.
- Do not use the project to disrupt services, bypass access controls, or interfere with other players.

---

## ⚠️ Responsible Use

This repository is provided for **educational, testing, and research purposes**. Users are responsible for complying with applicable laws, platform rules, game terms, and network policies.

The author does not encourage unauthorized access, cheating, abuse, service disruption, credential theft, or interference with third-party accounts or infrastructure.

---

## 🤝 Contributing

Contributions that improve code quality, documentation, reliability, and educational value are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test your changes in an authorized environment.
5. Open a pull request with a clear description.

Please **never include real credentials or private tokens** in pull requests.

---

## 👨‍💻 Maintainer

<div align="center">

### Hussnain sK

**Developer & Repository Owner**

<a href="https://github.com/HussnainsK">
  <img src="https://img.shields.io/badge/GitHub-HussnainsK-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</a>

</div>

---

## 📜 License

No explicit open-source license is currently specified in this README. Unless a license is added to the repository, users should not assume that the code may be freely redistributed or modified beyond the permissions granted by GitHub's repository access and applicable law.

---

## ⭐ Support

If you find the project useful for learning or research, consider giving the repository a ⭐.

<div align="center">

**BUILD • TEST • LEARN • IMPROVE**

[⭐ Star Repository](https://github.com/HussnainsK/Free-Fire-TCPBOT-OB54)

</div>
