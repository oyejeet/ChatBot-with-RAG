import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

# Set Google API Key
GOOGLE_API_KEY = "AIzaSyC67N9Gtw95ndsSLiwYT9e6gyVIDiPiL28"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def setup_gemini_models():
    """Setup Gemini models with fallback options"""
    # Try different models in order of preference
    models_to_try = ["gemini-1.5-flash", "gemini-1.5-pro"]
    
    for model_name in models_to_try:
        try:
            print(f"Trying to initialize {model_name}...")
            llm = ChatGoogleGenerativeAI(model=model_name)
            # Test with a simple query
            test_response = llm.invoke("Hello")
            print(f"✅ Successfully initialized {model_name}")
            return llm
        except Exception as e:
            print(f"❌ {model_name} failed: {e}")
            continue
    
    raise Exception("No Gemini models could be initialized")

def create_sample_documents():
    """Create sample documents for demonstration"""
    sample_texts = [
        "The Universal Declaration of Human Rights states that all human beings are born free and equal in dignity and rights.",
        "Article 1: All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience.",
        "Article 2: Everyone is entitled to all the rights and freedoms set forth in this Declaration, without distinction of any kind.",
        "Article 3: Everyone has the right to life, liberty and security of person.",
        "Article 4: No one shall be held in slavery or servitude; slavery and the slave trade shall be prohibited in all their forms."
    ]
    
    from langchain_core.documents import Document
    documents = [Document(page_content=text, metadata={"source": "sample"}) for text in sample_texts]
    return documents

def create_vector_store(documents):
    """Create a vector store from documents"""
    print("Creating text chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        add_start_index=True
    )
    text_chunks = text_splitter.split_documents(documents)
    print(f"Created {len(text_chunks)} text chunks")
    
    print("Initializing embeddings model...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    print("Creating vector store...")
    vector_store = FAISS.from_documents(text_chunks, embeddings)
    print("✅ Vector store created successfully!")
    
    return vector_store

def answer_question(vector_store, llm, question):
    """Answer a question using RAG"""
    print(f"\n🔍 Searching for relevant documents...")
    relevant_docs = vector_store.similarity_search(question, k=2)
    
    print(f"📄 Found {len(relevant_docs)} relevant documents")
    for i, doc in enumerate(relevant_docs):
        print(f"  Document {i+1}: {doc.page_content[:100]}...")
    
    # Create context from relevant documents
    context = "\n\n".join([doc.page_content for doc in relevant_docs])
    
    # Create prompt template
    prompt_template = """
    Use the following context to answer the question. If you don't know the answer, say so.
    
    Context: {context}
    
    Question: {question}
    
    Answer:"""
    
    prompt = ChatPromptTemplate.from_template(prompt_template)
    
    # Generate answer
    print("🤖 Generating answer with Gemini...")
    chain = prompt | llm
    response = chain.invoke({"context": context, "question": question})
    
    return response.content

def main():
    print("🚀 Gemini RAG System Demo")
    print("=" * 40)
    
    try:
        # Setup models
        print("\n1. Setting up Gemini models...")
        llm = setup_gemini_models()
        
        # Create sample documents
        print("\n2. Creating sample documents...")
        documents = create_sample_documents()
        
        # Create vector store
        print("\n3. Creating vector database...")
        vector_store = create_vector_store(documents)
        
        # Demo questions
        demo_questions = [
            "What does Article 1 of the Universal Declaration say?",
            "What rights are mentioned in Article 3?",
            "What is prohibited in Article 4?"
        ]
        
        print("\n4. Testing RAG system with sample questions...")
        for i, question in enumerate(demo_questions, 1):
            print(f"\n--- Question {i} ---")
            print(f"Q: {question}")
            
            try:
                answer = answer_question(vector_store, llm, question)
                print(f"A: {answer}")
            except Exception as e:
                print(f"❌ Error answering question: {e}")
                print("This might be due to rate limiting. Wait a few minutes and try again.")
        
        print("\n🎉 Demo completed successfully!")
        print("\nTo use this system with your own documents:")
        print("1. Run: streamlit run main_gemini.py")
        print("2. Upload your PDF documents")
        print("3. Ask questions about the content")
        
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        print("\nTroubleshooting tips:")
        print("- Check your internet connection")
        print("- Verify your Google API key is valid")
        print("- Wait a few minutes if you hit rate limits")
        print("- Try running the demo again later")

if __name__ == "__main__":
    main() 