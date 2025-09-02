import os

# Google API Configuration
GOOGLE_API_KEY = "AIzaSyC67N9Gtw95ndsSLiwYT9e6gyVIDiPiL28"

# Set environment variable
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Model Configuration - Updated with correct model names
GEMINI_MODELS = ["gemini-1.5-flash", "gemini-1.5-pro"]
DEFAULT_EMBEDDING_MODEL = "models/embedding-001"

# Vector Database Configuration
FAISS_DB_PATH = "vectorstore/db_faiss"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# PDF Configuration
PDFS_DIRECTORY = "pdfs/"

# Streamlit Configuration
STREAMLIT_TITLE = "AI Lawyer with Gemini API"
STREAMLIT_DESCRIPTION = "Upload a PDF and ask questions about legal documents using Google's Gemini AI" 