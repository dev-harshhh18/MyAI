
# Personal AI Chatbot Project

## Overview
This project is a personal AI chatbot using OpenAI's GPT API. It features encrypted conversation storage and retrieval, making it a secure and interactive AI assistant.

---

## Setup Guide

### Prerequisites
1. **Python**: Ensure Python 3.7 or later is installed. [Download Python](https://www.python.org/downloads/)
2. **Git**: Install Git for repository cloning. [Download Git](https://git-scm.com/)
3. **API Key**: Obtain an API key from OpenAI or another supported AI service.
4. **Encryption Key**: Generate a valid Fernet encryption key.

---

### Step 1: Clone the Repository
Use Git to clone the repository (replace `<repo-link>` with the actual link):
```bash
git clone <repo-link>
cd <project-folder>
```
Alternatively, download and extract the ZIP file.

---

### Step 2: Create a Virtual Environment
Set up a virtual environment to manage dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate  # For Linux/Mac
.venv\Scripts\activate   # For Windows
```

---

### Step 3: Install Dependencies
Install required Python packages:
```bash
pip install -r requirements.txt
```

---

### Step 4: Configure Environment Variables
1. Rename `.env.example` to `.env`:
   ```bash
   mv .env.example .env  # Linux/Mac
   rename .env.example .env  # Windows
   ```
2. Add your OpenAI API key and encryption key to `.env`:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ENCRYPTION_KEY=your_fernet_key
   ```

- **OpenAI API Key**: Get from [OpenAI](https://platform.openai.com/signup/).
- **Encryption Key**: Generate using:
  ```python
  from cryptography.fernet import Fernet
  print(Fernet.generate_key().decode())
  ```

---

### Step 5: Run the Program
Start the chatbot:
```bash
python3 main.py
```

---

### Step 6: Interact with the Chatbot
- **Send Messages**: Type a message to receive AI responses.
- **Retrieve Conversations**: Use the command `retrieve [keyword]` (replace `[keyword]` with your keyword).
- **Exit Program**: Type `exit`.

---

## Notes
- **Encrypted Logs**: Conversations are stored in `conversations.log` using encryption. Protect this file.
- **Error Handling**: Handles rate-limit errors and other issues.
- **Fernet Key**: Always use the same key for decryption.

---

## Troubleshooting
- **Invalid Encryption Key**: Ensure your Fernet key is 32 characters long and base64-encoded.
- **Rate Limit Errors**: Upgrade your API plan or add delays.
- **Dependencies Issues**: Reinstall dependencies with `pip install -r requirements.txt`.

---

## License
This project is open-source under the [MIT License](LICENSE).

---

### Contributors
Feel free to contribute by submitting issues or pull requests! 😊
