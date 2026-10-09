# 🐰 BunBun AI — RAG Chatbot

BunBun AI is a friendly chatbot designed to answer questions using information from an uploaded knowledge base.

## ✨ Features

* Chat interface built with Streamlit.
* Upload a TXT file as a knowledge base.
* Use knowledge-base context to answer questions.
* Generate responses using Ollama.
* Clear the conversation when needed.

## 🛠️ Technologies

* Python
* Streamlit
* Ollama
* Llama 3.2

## 📋 Requirements

* Python 3.10 or newer
* Ollama installed and running
* The `llama3.2` model downloaded in Ollama

## 🚀 Run Locally

### 1. Install the dependencies

```bash
pip install streamlit ollama
```

### 2. Download the AI model

```bash
ollama pull llama3.2
```

### 3. Start the chatbot

```bash
python -m streamlit run app.py
```

Open the local address displayed in your terminal, usually `http://localhost:8501`.

## 📚 How to Use

1. Start BunBun AI.
2. Upload a TXT file containing your knowledge-base information.
3. Enter a question in the chat box.
4. BunBun uses the uploaded text as context to generate an answer.

## ⚠️ Notes

This initial version uses uploaded text as context. Semantic retrieval and embeddings can be added in a later version to provide a fuller Retrieval-Augmented Generation (RAG) pipeline.

GitHub stores the source code; it does not automatically run the Ollama model.

## 👩‍💻 Project Status

Initial prototype — under development.
s
