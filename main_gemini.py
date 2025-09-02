import streamlit as st
import os
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from config import *

custom_prompt_template = """
Use the pieces of information provided in the context to answer user's question.
If you dont know the answer, just say that you dont know, dont try to make up an answer. 
Dont provide anything out of the given context
Question: {question} 
Context: {context} 
Answer:
"""

# Use Google's text embedding model
embeddings = GoogleGenerativeAIEmbeddings(model=DEFAULT_EMBEDDING_MODEL)
# Use Gemini Pro model (fallback to 1.0-pro if 1.5-pro has rate limits)
try:
    llm_model = ChatGoogleGenerativeAI(model=GEMINI_MODELS[1])  # gemini-1.5-pro
except Exception as e:
    st.warning("Gemini 1.5 Pro unavailable, falling back to Gemini 1.0 Pro")
    llm_model = ChatGoogleGenerativeAI(model=GEMINI_MODELS[0])  # gemini-1.0-pro

def upload_pdf(file):
    with open(PDFS_DIRECTORY + file.name, "wb") as f:
        f.write(file.getbuffer())

def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents

def create_chunks(documents): 
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = CHUNK_SIZE,
        chunk_overlap = CHUNK_OVERLAP,
        add_start_index = True
    )
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks

def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(model=DEFAULT_EMBEDDING_MODEL)

def create_vector_store(db_faiss_path, text_chunks):
    faiss_db = FAISS.from_documents(text_chunks, get_embedding_model())
    faiss_db.save_local(db_faiss_path)
    return faiss_db

def retrieve_docs(faiss_db, query):
    return faiss_db.similarity_search(query)

def get_context(documents):
    context = "\n\n".join([doc.page_content for doc in documents])
    return context

def answer_query(documents, model, query):
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | model
    return chain.invoke({"question": query, "context": context})

# Streamlit UI
st.title(STREAMLIT_TITLE)
st.write(STREAMLIT_DESCRIPTION)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf",
    accept_multiple_files=False
)

user_query = st.text_area("Enter your prompt: ", height=150, placeholder="Ask Anything!")

ask_question = st.button("Ask AI Lawyer")

if ask_question:
    if uploaded_file and user_query:
        # Create pdfs directory if it doesn't exist
        os.makedirs(PDFS_DIRECTORY, exist_ok=True)
        
        upload_pdf(uploaded_file)
        documents = load_pdf(PDFS_DIRECTORY + uploaded_file.name)
        text_chunks = create_chunks(documents)
        faiss_db = create_vector_store(FAISS_DB_PATH, text_chunks)

        retrieved_docs = retrieve_docs(faiss_db, user_query)
        response = answer_query(documents=retrieved_docs, model=llm_model, query=user_query)

        st.chat_message("user").write(user_query)
        st.chat_message("AI Lawyer (Gemini)").write(response.content)

    else:
        st.error("Kindly upload a valid PDF file and/or ask a valid Question!") 