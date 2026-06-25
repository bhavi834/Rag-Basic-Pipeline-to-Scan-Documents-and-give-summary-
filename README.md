# Rag-Basic-Pipeline-for-Documents
📄 PDF RAG Chatbot using FAISS + Gemini 2.5 Flash

A simple Retrieval-Augmented Generation (RAG) chatbot that answers questions from PDF documents using LangChain, HuggingFace Embeddings, FAISS, and Google Gemini 2.5 Flash.

Features
Read one or multiple PDF documents
Automatically split documents into chunks
Generate semantic embeddings using HuggingFace
Store embeddings in a FAISS vector database
Retrieve relevant document chunks
Generate intelligent answers using Gemini 2.5 Flash
Display document source and page number
Easy to extend with Streamlit UI

Project Architecture:-
PDF Documents
      │
      ▼
PyPDFLoader
      │
      ▼
Text Extraction
      │
      ▼
Chunking
      │
      ▼
all-MiniLM-L6-v2
(Embedding Model)
      │
      ▼
FAISS Vector Store
      │
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

User Question
      │
      ▼
Question Embedding
      │
      ▼
Similarity Search
      │
      ▼
Top Relevant Chunks
      │
      ▼
Gemini 2.5 Flash
      │
      ▼
Final Answer
Folder Structure
pdf-rag/
│
├── documents/
│      ├── pdf1.pdf
│      ├── pdf2.pdf
│
├── vectorstore/
│      ├── ingest.py
│      ├── chatbot.py
│      ├── app.py
│      ├── requirements.txt
│      ├── .env
│      │
│      └── faiss_index/
│             ├── index.faiss
│             └── index.pkl
│
└── README.md
Technologies Used
Component	Technology
Programming Language	Python 3.11+
Framework	LangChain
PDF Loader	PyPDFLoader
Embedding Model	sentence-transformers/all-MiniLM-L6-v2
Vector Database	FAISS
LLM	Google Gemini 2.5 Flash
Embedding Provider	HuggingFace
UI (Optional)	Streamlit
Installation
Step 1

Clone the repository

git clone https://github.com/yourusername/pdf-rag.git

cd pdf-rag
Step 2

Create Virtual Environment

Windows

python -m venv venv

Activate

venv\Scripts\activate

Linux / Mac

source venv/bin/activate
Step 3

Install Dependencies

pip install -r requirements.txt
Step 4

Create a Google AI Studio API Key

Visit

https://aistudio.google.com

Create an API key.

Step 5

Create a .env file

GOOGLE_API_KEY=YOUR_API_KEY

Example

GOOGLE_API_KEY=AIza.....................
Adding PDF Files

Place all PDF files inside

documents/

Example

documents/
│
├── ISO9001.pdf
├── LabourCode.pdf
├── EmployeeHandbook.pdf
Creating the Vector Database

Run

python ingest.py

This will

Read all PDFs
Extract text
Split into chunks
Generate embeddings
Store vectors inside
faiss_index/

Files created

index.faiss

index.pkl
Running the Chatbot

Run

python chatbot.py

Example

Ask Question:

What is ISO 9001?

Output

Answer:

ISO 9001 is an international standard for Quality
Management Systems that specifies requirements for
organizations to consistently provide products and
services that meet customer and regulatory
requirements.

Source:
ISO9001.pdf
Page 12
Running Streamlit UI

If Streamlit UI is available

streamlit run app.py

Open

http://localhost:8501
Workflow
1. Document Loading

Reads PDF files using

PyPDFLoader
2. Chunking

Documents are divided into

Chunk Size = 1000

Overlap = 200
3. Embedding Generation

Uses

sentence-transformers/all-MiniLM-L6-v2

Each chunk is converted into a numerical vector.

4. Vector Storage

Embeddings are stored inside

FAISS

for efficient semantic search.

5. User Query

The user's question is converted into an embedding using the same embedding model.

6. Similarity Search

FAISS retrieves the most relevant document chunks.

7. Answer Generation

Retrieved chunks are sent to

Gemini 2.5 Flash

which generates the final answer.

Models Used
Embedding Model
sentence-transformers/all-MiniLM-L6-v2

Purpose

Generate document embeddings
Generate question embeddings
Semantic similarity search
Large Language Model
Gemini 2.5 Flash

Purpose

Understand retrieved context
Generate natural language answers
Summarize information
Answer user queries
Dependencies


Sample Questions
Summarize the document.

What is the purpose of this report?

Who prepared this report?

Explain Chapter 5.

List the key recommendations.

What are the planning requirements?

What risks are identified?

Compare section 4 and section 5.

Provide a short summary.

What are the conclusions?


Current version supports:

Text-based PDFs
Multiple PDF documents
Semantic search
Context-based question answering

The current version does not support:

Scanned PDFs (OCR)
Tables extraction
Images
Charts
Figures
Handwritten documents
Multimodal retrieval
Future Improvements
OCR using Tesseract/EasyOCR
Table extraction using Camelot or pdfplumber
Image understanding using Gemini Vision
Hybrid Search (BM25 + Vector Search)
Reranking using BAAI BGE Reranker
ChromaDB/Pinecone integration
Chat history and memory
Source citations with highlighted text
Cloud deployment (AWS/Azure/GCP)
Docker support
Authentication and user management
