# 🤖 SANDEEPA AI — Personal AI Assistant

An AI-powered personal assistant built with Python, Flask, and the OpenAI API.

<p align="center">
  <strong>Intelligent Conversations · Persistent Memory · Sinhala & English</strong>
</p>

---

## 🌟 Overview

SANDEEPA AI is a web-based personal AI assistant designed to provide helpful and natural conversations in Sinhala and English.

Built with Python, Flask, and the OpenAI API, it combines conversational AI with persistent chat history, personal memory management, optional web search, and a customizable user interface.

This project is part of an ongoing journey into AI Engineering and intelligent software development.

## ✨ Features

- 🤖 AI-powered conversations using the OpenAI API
- 🌐 Sinhala and English language support
- 💬 Persistent conversation history using SQLite
- 🗂️ Create, load, and delete conversations
- 🧠 Personal Memory Center
- 💾 Save and manage personal memories
- 🔎 Optional web search for current information
- 🎨 Dark, Light, and Warm themes
- 📱 Responsive web interface
- 🔐 Environment-based API key management

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Flask | Web application framework |
| OpenAI API | AI intelligence |
| SQLite | Persistent data storage |
| HTML | Web structure |
| CSS | Interface design |
| JavaScript | Frontend functionality |
| python-dotenv | Environment configuration |

## 🖼️ Screenshots

### Screenshot 1
![SANDEEPA AI Screenshot 1](screenshots/SANDEEPA%20AI%20screenshots%201.png)

### Screenshot 2
![SANDEEPA AI Screenshot 2](screenshots/SANDEEPA%20AI%20screenshots%202.png)

### Screenshot 3
![SANDEEPA AI Screenshot 3](screenshots/SANDEEPA%20AI%20screenshots%203.png)

### Screenshot 4
![SANDEEPA AI Screenshot 4](screenshots/SANDEEPA%20AI%20screenshots.png)

---

## 📁 Project Structure

```text
SANDEEPA-AI-ASSISTANT/
│
├── templates/
│   ├── index.html
│   └── memory.html
│
├── .env.example
├── .gitignore
├── README.md
├── app.py
├── web_app.py
├── database.py
└── requirements.txt
```

Local-only files such as `.env`, `.venv/`, and `sandeepa_ai.db` are not included in the public repository.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sandeepawijesinghe/SANDEEPA-AI-ASSISTANT.git
```

```bash
cd SANDEEPA-AI-ASSISTANT
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root directory.

Add your own configuration:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-5.5
ENABLE_WEB_SEARCH=true
```

Never publish your real API key.

### 6. Run the application

```bash
python web_app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

## 💡 Usage

1. Start the SANDEEPA AI application.
2. Open the local web address.
3. Start a new conversation.
4. Ask questions in Sinhala or English.
5. Manage conversations through Chat History.
6. Save personal information through the Memory Center.
7. Customize the interface using the available themes.

## 🔐 Security

- API keys are stored in local environment variables.
- `.env` is excluded from Git.
- Local database files are excluded from Git.
- Private user data and credentials should never be published.

**Important:** This project is currently intended for local development and personal use. Additional authentication, deployment configuration, and production security measures are required before public deployment.

## 🗺️ Future Development

Planned improvements include:

- Advanced Retrieval-Augmented Generation (RAG)
- Voice interaction
- Improved long-term personalization
- Advanced AI agent capabilities
- Enhanced security and authentication
- More intelligent assistant features

## 👨‍💻 Developer

**Sandeepa Wijesinghe**

Aspiring AI Engineer | Mechatronics & Robotics Enthusiast

Interested in Artificial Intelligence, Agentic AI, Generative AI, Robotics, and Intelligent Automation.

**GitHub:** [Sandeepawijesinghe](https://github.com/Sandeepawijesinghe)
---

<p align="center">
  <strong>Building Intelligent Systems, One Project at a Time. 🚀</strong>
</p>
