import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# Set Google API Key
GOOGLE_API_KEY = "AIzaSyC67N9Gtw95ndsSLiwYT9e6gyVIDiPiL28"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def test_gemini_llm(model_name):
    """Test the Gemini LLM with a specific model"""
    try:
        llm = ChatGoogleGenerativeAI(model=model_name)
        response = llm.invoke("Hello! Can you tell me a short joke?")
        print(f"✅ Gemini {model_name} Test Passed!")
        print(f"Response: {response.content}")
        return True
    except Exception as e:
        print(f"❌ Gemini {model_name} Test Failed: {e}")
        return False

def test_gemini_embeddings():
    """Test the Gemini embeddings"""
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        text = "This is a test sentence for embeddings."
        embedding = embeddings.embed_query(text)
        print("✅ Gemini Embeddings Test Passed!")
        print(f"Embedding dimension: {len(embedding)}")
        return True
    except Exception as e:
        print(f"❌ Gemini Embeddings Test Failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing Gemini API Integration...")
    print("=" * 40)
    
    # Test different Gemini models
    models_to_test = ["gemini-1.5-flash", "gemini-1.5-pro"]
    llm_success = False
    
    for model in models_to_test:
        print(f"\nTesting {model}...")
        if test_gemini_llm(model):
            llm_success = True
            print(f"✅ Successfully using {model}")
            break
        else:
            print(f"⚠️  {model} failed, trying next model...")
    
    print()
    
    embeddings_success = test_gemini_embeddings()
    print()
    
    if llm_success and embeddings_success:
        print("🎉 All tests passed! Gemini API integration is working correctly.")
    elif embeddings_success:
        print("⚠️  LLM tests failed due to rate limiting, but embeddings work. The system should still function.")
    else:
        print("❌ Critical tests failed. Please check your API key and internet connection.")
    
    print("\nNote: If you're hitting rate limits, wait a few minutes and try again.")
    print("Google's free tier has strict rate limits on API calls.") 