import os
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

# Set Google API Key
GOOGLE_API_KEY = "AIzaSyC67N9Gtw95ndsSLiwYT9e6gyVIDiPiL28"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Step 1: Upload & Load raw PDF(s)
pdfs_directory = 'pdfs/'

def upload_pdf(file):
    with open(pdfs_directory + file.name, "wb") as f:
        f.write(file.getbuffer())

def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents

# Load the Universal Declaration of Human Rights PDF
file_path = 'universal_declaration_of_human_rights.pdf'
documents = load_pdf(file_path)
print("PDF pages: ", len(documents))

# Step 2: Create Chunks
def create_chunks(documents): 
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        add_start_index = True
    )
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks

text_chunks = create_chunks(documents)
print("Chunks count: ", len(text_chunks))

# Step 3: Setup Embeddings Model (Use Google's text embedding model)
def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Step 4: Index Documents **Store embeddings in FAISS (vector store)
FAISS_DB_PATH = "vectorstore/db_faiss"
faiss_db = FAISS.from_documents(text_chunks, get_embedding_model())
faiss_db.save_local(FAISS_DB_PATH)
print("Vector database created and saved successfully!") 