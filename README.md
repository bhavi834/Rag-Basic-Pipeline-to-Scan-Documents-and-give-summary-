# 📄 PDF RAG Chatbot using FAISS + Gemini 2.5 Flash

A Retrieval-Augmented Generation (RAG) chatbot that answers questions from PDF documents using LangChain, HuggingFace Embeddings, FAISS, and Google Gemini 2.5 Flash.

## 🚀 Features

* Supports single and multiple PDF documents
* Extracts and chunks PDF text automatically
* Generates semantic embeddings using HuggingFace
* Stores embeddings using FAISS
* Retrieves relevant document sections for answering queries
* Generates context-aware responses using Gemini 2.5 Flash
* Displays document source and page references

## 🏗️ Architecture

PDF Documents
      │
      ▼
Text Extraction
      │
      ▼
Chunking
      │
      ▼
Embeddings (MiniLM)
      │
      ▼
FAISS Vector Store
      │
────────────────────

User Query
      │
      ▼
Similarity Search
      │
      ▼
Relevant Chunks
      │
      ▼
Gemini 2.5 Flash
      │
      ▼
Final Response

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** LangChain
* **PDF Loader:** PyPDFLoader
* **Embedding Model:** all-MiniLM-L6-v2
* **Vector Database:** FAISS
* **LLM:** Google Gemini 2.5 Flash

## ⚙️ Setup

1. Clone the repository

git clone https://github.com/bhavi834/Rag-Basic-Pipeline-to-Scan-Documents-and-give-summary-.git

2. Install dependencies

pip install -r requirements.txt

3. Add your Google API key in a `.env` file

GOOGLE_API_KEY=YOUR_API_KEY

4. Place PDF files inside the documents/ folder.

5. Create embeddings

python ingest.py

6. Start the chatbot

python chatbot.py

## 💡 Sample Questions

* Summarize the document.
* Explain a specific chapter.
* List key recommendations.
* What are the identified risks?
* Compare different sections of the document.

## 🔮 Future Enhancements

* OCR support for scanned PDFs
* Table and image extraction
* Hybrid search implementation
* Chat memory support
* Cloud deployment and Docker support
