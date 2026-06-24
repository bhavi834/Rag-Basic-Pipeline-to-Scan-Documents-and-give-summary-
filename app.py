import os
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 PDF RAG Chatbot")
st.write("Ask questions from your PDF documents")

# =========================
# LOAD API KEY
# =========================
load_dotenv()

api_key = os.getenv("AQ.Ab8RN6KcWXTXJ_zEJ-hO-WSZA93TrcapCPTb7ep3elGG_yGhEg")

if not api_key:
    st.error("GEMINI_API_KEY not found in .env file")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# =========================
# LOAD EMBEDDINGS
# =========================
@st.cache_resource
def load_vector_db():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db

db = load_vector_db()

# =========================
# QUESTION INPUT
# =========================
question = st.text_input(
    "Ask a question about the document"
)

if st.button("Submit"):

    if not question:
        st.warning("Please enter a question")
        st.stop()

    with st.spinner("Searching document..."):

        docs = db.similarity_search(
            question,
            k=5
        )

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are a helpful document assistant.

Answer ONLY from the provided context.

Context:
{context}

Question:
{question}

If the answer is not available in the context,
say "I could not find the answer in the document."
"""

        response = model.generate_content(prompt)

    st.subheader("Answer")
    st.write(response.text)

    st.subheader("Sources")

    for i, doc in enumerate(docs, start=1):

        source = doc.metadata.get(
            "source_file",
            "Unknown"
        )

        page = doc.metadata.get(
            "page",
            "Unknown"
        )

        st.write(
            f"{i}. {source} | Page {page}"
        )

    with st.expander("Retrieved Context"):

        for i, doc in enumerate(docs, start=1):

            st.markdown(f"### Chunk {i}")
            st.write(doc.page_content[:1000])