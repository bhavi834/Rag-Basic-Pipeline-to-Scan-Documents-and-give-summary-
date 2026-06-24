import os
import google.generativeai as genai

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# ==========================
# Load Gemini API Key
# ==========================
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# ==========================
# Load Embeddings
# ==========================
print("Loading embeddings...")
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    cache_folder=r"C:\Users\Admin\.cache\huggingface\hub"
)
# ==========================
# Load FAISS Index
# ==========================
print("Loading FAISS index...")

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

print("\n===================================")
print("     GEMINI RAG CHATBOT READY")
print("===================================")
print("Type 'exit' to quit")

while True:

    question = input("\nAsk Question: ").strip()

    if question.lower() == "exit":
        break

    print("\nSearching document...")

results = db.similarity_search_with_score(
    question,
    k=5
)

    if not docs:
        print("No relevant information found.")
        continue

    # Build Context
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the information provided in the context.

Context:
{context}

Question:
{question}

If the answer is not available in the context, say:
'I could not find the answer in the document.'
"""

    print("\nGenerating answer...\n")

    response = model.generate_content(prompt)

    print("=" * 60)
    print("ANSWER")
    print("=" * 60)
    print(response.text)

    print("\n" + "=" * 60)
    print("SOURCES")
    print("=" * 60)

    for i, doc in enumerate(docs, start=1):

d.metadata["source_file"] = file
d.metadata["page"] = page

        print(f"{i}. {source} | Page: {page}")