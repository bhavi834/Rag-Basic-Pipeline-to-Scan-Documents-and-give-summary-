import os

print("STEP 1 - Imports starting")

from langchain_community.document_loaders import PyPDFLoader
print("STEP 2 - PyPDFLoader imported")

from langchain_text_splitters import RecursiveCharacterTextSplitter
print("STEP 3 - Text splitter imported")

from langchain_huggingface import HuggingFaceEmbeddings
print("STEP 4 - HuggingFace imported")

from langchain_community.vectorstores import FAISS
print("STEP 5 - FAISS imported")

pdf_folder = r"..\documents"

print("STEP 6 - Checking documents folder")

pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

print(f"Found PDFs: {pdf_files}")

all_docs = []

for file in pdf_files:
    print(f"Loading PDF: {file}")

    loader = PyPDFLoader(os.path.join(pdf_folder, file))
    docs = loader.load()

    print(f"Pages loaded: {len(docs)}")

    all_docs.extend(docs)

print("STEP 7 - Splitting")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(all_docs)

print(f"Chunks created: {len(chunks)}")

print("STEP 8 - Loading embedding model")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("STEP 9 - Creating FAISS index")

db = FAISS.from_documents(chunks, embeddings)

print("STEP 10 - Saving")

db.save_local("faiss_index")

print("SUCCESS")