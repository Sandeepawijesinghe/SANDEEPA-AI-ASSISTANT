# SANDEEPA AI — Personal AI Assistant

An AI-powered personal assistant built with Python, Flask, and the OpenAI API.

## Overview

SANDEEPA AI is a web-based personal AI assistant designed to provide helpful, natural conversations in Sinhala and English.

Powered by the OpenAI API, it offers an interactive chat experience with persistent conversation history, a memory center, optional web search, and multiple visual themes.

This project is developed as a practical AI Engineering learning project.

## Features

- AI-powered conversations using the OpenAI API
- Sinhala and English language support
- Persistent chat history using SQLite
- Create, load, and delete conversations
- Personal Memory Center
- Save and manage personal memories
- Optional web search for current information
- Dark, Light, and Warm themes
- Responsive web interface
- Basic error handling
- Environment-based API key management

## Technologies Used

- Python
- Flask
- OpenAI API
- OpenAI Python SDK
- SQLite
- HTML
- CSS
- JavaScript
- python-dotenv

## Project Structure

```text
SANDEEPA-AI-ASSISTANT/
│
├── .venv/
├── templates/
│   ├── index.html
│   └── memory.html
│
├── .env                  # Private environment variables
├── .env.example          # Environment variable template
├── .gitignore
├── app.py
├── web_app.py            # Main Flask application
├── database.py
├── requirements.txt
├── README.md
└── sandeepa_ai.db        # Local SQLite database
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd SANDEEPA-AI-ASSISTANT
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

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

Add your own OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-5.5
ENABLE_WEB_SEARCH=true
```

Never upload your real `.env` file or share your API key.

### 6. Run the application

```bash
python web_app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Usage

1. Start SANDEEPA AI.
2. Open the local web address in your browser.
3. Start a new conversation.
4. Ask questions in Sinhala or English.
5. Use the Memory Center to save and manage memories.
6. Access previous conversations through Chat History.
7. Change the interface theme according to your preference.

## Security

- API keys are stored in a local `.env` file.
- `.env` is excluded from Git using `.gitignore`.
- Local SQLite database files are excluded from Git.
- Never publish API keys, passwords, or private user data.
- This project is currently intended for local development and personal use.

Additional authentication and production security measures are required before public deployment.

## Current Development Status

SANDEEPA AI is an actively developed personal AI assistant.

The current version includes the core chat interface, OpenAI integration, conversation history, memory management, and theme selection.

Future improvements may include advanced RAG capabilities, voice interaction, improved personalization, and additional AI agent features.

## Author

**SANDEEPA AI PROJECT**

Created as a practical AI Engineering learning project.

**Project Focus:** Artificial Intelligence, Python Development, and Agentic AI.