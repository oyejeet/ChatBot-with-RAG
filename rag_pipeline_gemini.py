import os
from langchain_google_genai import ChatGoogleGenerativeAI
from vector_database_gemini import faiss_db
from langchain_core.prompts import ChatPromptTemplate

# Set Google API Key
GOOGLE_API_KEY = "AIzaSyC67N9Gtw95ndsSLiwYT9e6gyVIDiPiL28"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Step 1: Setup LLM (Use Gemini Pro with fallback)
try:
    llm_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
except Exception as e:
    print("Gemini 1.5 Pro unavailable, falling back to Gemini 1.0 Pro")
    llm_model = ChatGoogleGenerativeAI(model="gemini-1.0-pro")

# Step 2: Retrieve Docs
def retrieve_docs(query):
    return faiss_db.similarity_search(query)

def get_context(documents):
    context = "\n\n".join([doc.page_content for doc in documents])
    return context

# Step 3: Answer Question
custom_prompt_template = """
Use the pieces of information provided in the context to answer user's question.
If you dont know the answer, just say that you dont know, dont try to make up an answer. 
Dont provide anything out of the given context
Question: {question} 
Context: {context} 
Answer:
"""

def answer_query(documents, model, query):
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | model
    return chain.invoke({"question": query, "context": context})

# Example usage
# question = "If a government forbids the right to assemble peacefully which articles are violated and why?"
# retrieved_docs = retrieve_docs(question)
# print("AI Lawyer: ", answer_query(documents=retrieved_docs, model=llm_model, query=question)) 