# 🤖 Rushi's AI Bot (Django + Ollama)

A simple AI chatbot built using Django backend and Ollama local LLM.

---

## 📌 Tech Stack Used

- Python 3.10+
- Django
- Requests
- Ollama (Local LLM server)
- TinyLlama / Gemma Model

---

## 🖥 System Requirements

- 8GB RAM minimum
- Windows / Mac / Linux
- Python installed
- Ollama installed

---

## ⚙️ Step 1: Clone Project

bash
git clone <your-repo-url>
cd project-folder


---

## ⚙️ Step 2: Create Virtual Environment

bash
python -m venv venv


Activate:

Windows:
bash
venv\Scripts\activate


Mac/Linux:
bash
source venv/bin/activate


---

## ⚙️ Step 3: Install Requirements

bash
pip install -r requirements.txt


---

## ⚙️ Step 4: Install Ollama

Download from:
https://ollama.com

After install, verify:

bash
ollama --version


---

## ⚙️ Step 5: Pull Model

Recommended lightweight model:

bash
ollama pull tinyllama


OR

bash
ollama pull gemma:2b


Check installed models:

bash
ollama list


---

## ⚙️ Step 6: Start Ollama Server

bash
ollama serve


(Default runs on http://127.0.0.1:11434)

⚠️ If port already in use, Ollama is already running.

---

## ⚙️ Step 7: Run Django Server

bash
python manage.py migrate
python manage.py runserver


Open browser:


http://127.0.0.1:8000/chat/


---

## 🔌 API Used

Ollama API Endpoint:


POST http://127.0.0.1:11434/api/generate


Request JSON:

json
{
  "model": "tinyllama:latest",
  "prompt": "Hello",
  "stream": false
}


---

## 🧠 Features

- Dark UI
- Instant reply feel
- Online status indicator
- Local LLM (No OpenAI key required)
- Fully offline AI chatbot

---

## 🚀 Performance Notes

- First reply may take 8–15 seconds (model loading)
- Subsequent replies are faster (2–4 seconds)
- Works best on 8GB+ RAM systems

---

## 🛠 Dependencies

requirements.txt:


Django>=4.2,<6.0
requests>=2.31.0


Install with:

bash
pip install -r requirements.txt


---

## 🛑 Common Issues

### Port 11434 already in use
Ollama already running. Do NOT start again.

### Slow first reply
Normal behavior (model loading).

### No reply
Check:
- Ollama running?
- Correct model name in views.py?
- Correct API URL?

---

## 👨‍💻 Developed By

Rushi