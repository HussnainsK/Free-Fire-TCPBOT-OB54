<div align="center">

⚡ FREE FIRE TCP BOT — OB54

Professional Python TCP Bot Project

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

📌 Overview

Free-Fire-TCPBOT-OB54 is a Python networking project built around TCP-style bot functionality, Protocol Buffers, encoded request payloads, and authenticated HTTP requests.

The repository is primarily intended for learning, testing, and protocol research in controlled environments.

Disclaimer: This is an independent community project. It is not affiliated with, sponsored by, or endorsed by Garena or Free Fire.

✨ Highlights

Python-based implementation

TCP/networking functionality

Protocol Buffer message modules

Bearer-token authentication for authenticated requests

Encoded request/response processing

Player/profile request handling

OB54-oriented protocol data

Simple, modular project layout

🧱 System Architecture

The Free-Fire-TCPBOT-OB54 project follows a layered request-processing architecture. Each layer is responsible for a specific part of the workflow, starting from the user command and ending with the processed response.

                    ⚡  F R E E  F I R E  T C P  B O T
                                      │
                                      ▼
                         👤  U S E R  /  B O T
                                      │
                                      │  Command / Action
                                      ▼
                         🐍  A P P L I C A T I O N
                                      │
                                      │  app.py
                                      ▼
                       🧩  R E Q U E S T  B U I L D E R
                                      │
                                      │  UID / Parameters
                                      │  Payload / Action
                                      ▼
                         📦  P R O T O B U F  /  D A T A
                                      │
                                      │  Serialize structured data
                                      ▼
                         🔐  A U T H E N T I C A T I O N
                                      │
                                      │  Runtime authorization
                                      ▼
                          ⚙️  N E T W O R K  E N G I N E
                                      │
                                      │  xDL.py
                                      ▼
                           🌐  A P I  L A Y E R
                                      │
                                      │  Encoded HTTP Request
                                      ▼
                          🎯  G A M E  S E R V E R
                                      │
                                      │  Request Processing
                                      ▼
                         📡  R E S P O N S E  D A T A
                                      │
                                      │  Binary / Encoded Data
                                      ▼
                           🔍  D E C O D E R
                                      │
                                      │  Deserialize / Parse
                                      ▼
                        📊  D A T A  P R O C E S S O R
                                      │
                                      │  Interpret / Organize
                                      ▼
                           ✅  F I N A L  R E S U L T

🧩 Core Components

👤 User / Bot Layer

The workflow begins when the user or bot initiates an action.

Responsibilities:

Start a command or operation

Provide required input

Trigger the application workflow

Receive the final processed result

⬇️

🐍 Application Layer — app.py

app.py acts as the primary application layer.

Responsibilities:

Control the main application logic

Handle bot-side operations

Receive commands/actions

Prepare information required for a request

Pass processing to the networking layer

⬇️

🧩 Request Builder

The request-building stage prepares the information required for communication.

Typical data can include:

UID

Request parameters

Action information

Payload data

Required protocol structures

The prepared information is then passed to the encoding layer.

⬇️

📦 Protocol Buffer Layer — Pb2/

The Pb2/ directory contains generated Protocol Buffer message modules.

These modules provide structured message definitions used by the project.

Responsibilities:

Represent structured request data

Represent structured response data

Serialize message objects

Deserialize supported response structures

Examples present in the repository include:

Pb2/
├── MajoRLoGinrEq_pb2.py
├── MajoRLoGinrEs_pb2.py
├── DEcwHisPErMsG_pb2.py
├── GenWhisperMsg_pb2.py
├── PorTs_pb2.py
├── Team_msg_pb2.py
└── room_join_pb2.py

⬇️

🔐 Authentication Layer

Authenticated requests require runtime authorization information.

The networking code uses the Bearer authorization scheme.

Responsibilities:

Obtain runtime authorization data

Load the configured token

Attach authorization information to requests

Keep authentication data separate from normal payload data

🔒 Never expose real authentication tokens, passwords, or private credentials in a public repository.

⬇️

⚙️ Networking Engine — xDL.py

xDL.py is responsible for the networking side of the project.

Responsibilities include:

Request construction

Network communication

Authentication handling

Sending requests

Receiving responses

Processing returned data

This component connects the application logic with the configured API layer.

⬇️

🌐 API Layer

The API layer is responsible for transporting the prepared request to the configured endpoint.

The request can contain:

Application Data
       ↓
Structured Payload
       ↓
Encoded Data
       ↓
Authorization
       ↓
HTTP Request

⬇️

🎯 Server Layer

The server receives the request and processes it according to the endpoint and payload.

The project README describes this stage as the game-client/API endpoint responsible for receiving requests and returning response data.

⬇️

📡 Response Layer

The server response is returned to the networking layer.

The response may contain binary or encoded information that requires additional processing before it can be used by the application.

⬇️

🔍 Decoder / Parser

The response-processing stage converts the returned data into a form that the application can understand.

Processing may involve:

📡 Raw Response
      ↓
🔍 Decode
      ↓
📦 Deserialize
      ↓
🧩 Parse
      ↓
📊 Structured Data

⬇️

📊 Data Processor

The processed response is interpreted and organized according to the application's requirements.

Responsibilities:

Interpret decoded information

Extract useful values

Organize response data

Prepare the final result

⬇️

✅ Final Result

The final processed information is returned to the application or displayed to the user/bot.

🔗 Component Overview

Layer

Component

Responsibility

🎮

User / Bot

Starts commands and actions

🐍

app.py

Application and bot logic

⚡

xDL.py

Networking and request handling

📦

Pb2/

Protocol Buffer message structures

🔐

Auth Layer

Handles Bearer-token authorization

🌐

API Layer

Sends authenticated requests

📡

Response Layer

Receives and processes responses

🔄 Request Flow

🚀 Complete Request Workflow

🚀  W O R K F L O W  S T A R T
              │
              ▼
        👤 USER / BOT
              │
              │  Command / Action
              ▼
        🐍 APPLICATION
              │
              │  app.py
              ▼
       🧩 INPUT HANDLER
              │
              │  Validate / Prepare
              ▼
       📝 REQUEST DATA
              │
              │  UID / Parameters
              ▼
       📦 PROTOCOL DATA
              │
              │  Protocol Buffer
              ▼
       🔐 AUTHENTICATION
              │
              │  Bearer Authorization
              ▼
       ⚙️ NETWORK ENGINE
              │
              │  xDL.py
              ▼
          🌐 API
              │
              │  HTTP Request
              ▼
       🎯 GAME SERVER
              │
              │  Process Request
              ▼
       📡 RESPONSE
              │
              │  Encoded / Binary
              ▼
        🔍 DECODER
              │
              │  Decode / Parse
              ▼
       📊 PROCESSOR
              │
              │  Organize Data
              ▼
        🧾 RESULT
              │
              ▼
          ✅ OUTPUT

🔁 Detailed Data Flow

👤 USER / BOT
      │
      │  1️⃣ Start Action
      ▼
🐍 app.py
      │
      │  2️⃣ Handle Application Logic
      ▼
🧩 REQUEST BUILDER
      │
      │  3️⃣ Prepare UID + Parameters
      ▼
📦 Pb2/
      │
      │  4️⃣ Create Structured Message
      ▼
🔐 AUTHENTICATION
      │
      │  5️⃣ Attach Runtime Authorization
      ▼
⚙️ xDL.py
      │
      │  6️⃣ Build Network Request
      ▼
🌐 API LAYER
      │
      │  7️⃣ Transmit Request
      ▼
🎯 SERVER
      │
      │  8️⃣ Process Request
      ▼
📡 RESPONSE
      │
      │  9️⃣ Return Data
      ▼
🔍 DECODER
      │
      │  🔟 Decode / Deserialize
      ▼
📊 DATA PROCESSOR
      │
      │  1️⃣1️⃣ Interpret Response
      ▼
🧾 RESULT
      │
      │  1️⃣2️⃣ Return Processed Data
      ▼
✅ USER / BOT OUTPUT

🔀 Request → Response Lifecycle

                         🚀 START
                            │
                            ▼
                       👤 COMMAND
                            │
                            ▼
                       🐍 app.py
                            │
                            ▼
                    🧩 BUILD REQUEST
                            │
                            ▼
                     📦 ENCODE DATA
                            │
                            ▼
                    🔐 AUTHORIZE
                            │
                            ▼
                     ⚙️ xDL.py
                            │
                            ▼
                      🌐 API CALL
                            │
                            ▼
                     🎯 SERVER
                            │
                            ▼
                    📡 RESPONSE
                            │
                            ▼
                     🔍 DECODE
                            │
                            ▼
                    📊 PROCESS
                            │
                            ▼
                      🧾 RESULT
                            │
                            ▼
                       ✅ OUTPUT
                            │
                            ▼
                         🏁 END

🧠 Workflow Responsibilities

Stage

Component

Main Responsibility

Output

1️⃣

👤 User / Bot

Start operation

Command

2️⃣

🐍 app.py

Handle application logic

Prepared action

3️⃣

🧩 Request Builder

Build request data

Request structure

4️⃣

📦 Pb2/

Structure / serialize protocol data

Encoded message

5️⃣

🔐 Authentication

Provide runtime authorization

Authorized request

6️⃣

⚙️ xDL.py

Handle networking

Network request

7️⃣

🌐 API

Transport request

Server request

8️⃣

🎯 Server

Process request

Response

9️⃣

📡 Response Layer

Receive returned data

Raw response

🔟

🔍 Decoder

Decode / parse

Structured data

1️⃣1️⃣

📊 Processor

Interpret data

Processed result

1️⃣2️⃣

✅ Output

Return result

Final response

📤 Outbound Request

👤 User
  ↓
🐍 app.py
  ↓
🧩 Build Payload
  ↓
📦 Protocol Buffer
  ↓
🔐 Authentication
  ↓
⚙️ xDL.py
  ↓
🌐 API
  ↓
🎯 Server

📥 Inbound Response

🎯 Server
  ↓
📡 Response Data
  ↓
⚙️ xDL.py
  ↓
🔍 Decode
  ↓
📦 Deserialize
  ↓
📊 Process
  ↓
🐍 Application
  ↓
👤 User / Bot

⚡ One-Line Workflow

👤 USER → 🐍 APP → 🧩 REQUEST → 📦 PROTOBUF → 🔐 AUTH → ⚙️ NETWORK → 🌐 API → 🎯 SERVER → 📡 RESPONSE → 🔍 DECODE → 📊 PROCESS → ✅ RESULT

🔒 Security Boundary: Authentication tokens, credentials, session information, and private configuration must remain private. Never publish them in documentation, screenshots, source code, commits, or issue reports.

🔐 Authentication

The networking code uses Bearer-token authentication for authenticated game-client requests. This is different from a normal website session-based login.

Authentication components

Component

Responsibility

app.py

Main application and bot logic

xDL.py

Networking, token retrieval, request construction and response processing

Pb2/

Protocol Buffer message definitions

MajoRLoGinrEq_pb2.py

Login-request message definitions

MajoRLoGinrEs_pb2.py

Login-response message definitions

token.txt

Runtime token storage referenced by the networking code

token.json

Token/metadata file currently present in the repository

The current xDL.py implementation reads a runtime token from token.txt and places it in an HTTP Authorization header using the Bearer scheme. It also contains a background routine that periodically requests tokens from an external service and writes a selected token to token.txt.

🔒 Security: Never publish passwords, access tokens, session credentials, or other private authentication material. Any credential accidentally committed to a public repository should be revoked/rotated immediately.

📁 Repository Structure

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

📥 Installation

1. Clone

git clone https://github.com/HussnainsK/Free-Fire-TCPBOT-OB54.git
cd Free-Fire-TCPBOT-OB54

2. Verify Python

python --version

3. Install dependencies

python -m pip install -r requirements.txt

4. Configure secrets safely

Do not place real passwords or tokens directly in source code or commit them to GitHub.

For local development, prefer environment variables or an ignored configuration file:

TOKEN=<private-token>
UID=<authorized-test-account-uid>

Add local secret files to .gitignore before committing changes.

▶️ Running

After installing dependencies and configuring an authorized test environment:

python app.py

The exact runtime behavior depends on the current source code and deployment environment.

🛡️ Security Best Practices

Never publish credentials or session tokens.

Rotate credentials immediately if they are exposed.

Do not rely on deleting a secret file alone; exposed values can remain in Git history.

Keep local secret/configuration files out of version control.

Use environment variables or a dedicated secret manager for deployments.

Test only accounts and systems you are authorized to use.

Do not use the project to disrupt services, bypass access controls, or interfere with other players.

⚠️ Responsible Use

This repository is provided for educational, testing, and research purposes. Users are responsible for complying with applicable laws, platform rules, game terms, and network policies.

The author does not encourage unauthorized access, cheating, abuse, service disruption, credential theft, or interference with third-party accounts or infrastructure.

🤝 Contributing

Contributions that improve code quality, documentation, reliability, and educational value are welcome.

Fork the repository.

Create a feature branch.

Make your changes.

Test your changes in an authorized environment.

Open a pull request with a clear description.

Please never include real credentials or private tokens in pull requests.

👨‍💻 Maintainer

<div align="center">

Hussnain sK

Developer & Repository Owner

<a href="https://github.com/HussnainsK">
  <img src="https://img.shields.io/badge/GitHub-HussnainsK-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</a>

</div>

📜 License

No explicit open-source license is currently specified in this README. Unless a license is added to the repository, users should not assume that the code may be freely redistributed or modified beyond the permissions granted by GitHub's repository access and applicable law.

💖 Support This Project

If you find Free-Fire-TCPBOT-OB54 useful for learning, research, or development, consider supporting the project. Your support helps encourage continued development, documentation, and improvements.

<div align="center">

💰 Sponsorship

<a href="https://github.com/sponsors/HussnainsK">
  <img src="https://img.shields.io/badge/💖%20Sponsor%20This%20Project-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor This Project">
</a>

<br><br>

Every contribution is appreciated. ❤️

</div>

⭐ Support

If you find the project useful for learning or research, consider giving the repository a ⭐.

<div align="center">

BUILD • TEST • LEARN • IMPROVE

⭐ Star Repository

</div>
