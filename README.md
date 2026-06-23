# 📄 PDF Chatbot using Streamlit, LangChain, Ollama & Qdrant

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents, generate embeddings, store them in Qdrant Vector Database, and retrieve relevant information using semantic search.

## 🚀 Features

* Upload PDF documents
* Extract text using PyPDFLoader
* Split documents into chunks
* Generate embeddings using Ollama (`nomic-embed-text`)
* Store embeddings in Qdrant Vector Database
* Perform semantic similarity search
* Interactive Streamlit UI

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Ollama
* Qdrant
* PyPDF
* Recursive Character Text Splitter

## 📂 Project Structure

```text
project_2/
│
├── pdf_app.py          # Streamlit Frontend
├── agent_backend.py    # PDF Processing & Retrieval Logic
└── README.md
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot
```

### Create Virtual Environment

```bash
python -m venv vienv
```

### Activate Virtual Environment

Windows:

```bash
vienv\Scripts\activate
```

### Install Dependencies

```bash
pip install streamlit
pip install langchain-community
pip install langchain-text-splitters
pip install langchain-ollama
pip install langchain-qdrant
pip install qdrant-client
pip install pypdf
```

## 🐳 Start Qdrant

```bash
docker compose up -d
```

Verify:

```bash
docker ps
```

## 🤖 Setup Ollama

Pull embedding model:

```bash
ollama pull nomic-embed-text
```

Verify:

```bash
ollama list
```

## ▶️ Run Application

```bash
streamlit run pdf_app.py
```

Open:

```text
http://localhost:8501
```

## 🔄 Workflow

1. Upload a PDF document
2. Process PDF
3. Extract text and split into chunks
4. Generate embeddings using Ollama
5. Store vectors in Qdrant
6. Ask questions
7. Retrieve relevant chunks using similarity search

## Example Questions

* What is Python?
* Explain Object Oriented Programming.
* What are the key concepts discussed in the document?
* Summarize the contents of the PDF.

## Future Improvements

* Conversational Chat Interface
* LLM-based Answer Generation
* Multi-PDF Support
* Chat History
* Source Citations
* Hybrid Search

## Author

Poojitha
