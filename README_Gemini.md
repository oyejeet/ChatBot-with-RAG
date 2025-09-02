# AI Lawyer RAG System with Gemini API

This is a RAG (Retrieval-Augmented Generation) system that uses Google's Gemini API to provide legal document analysis and question-answering capabilities.

## Features

- **PDF Document Processing**: Upload and process PDF documents
- **Vector Database**: Uses FAISS for efficient document retrieval
- **Gemini AI Integration**: Powered by Google's Gemini 1.5 Pro model
- **Text Embeddings**: Uses Google's text embedding model for semantic search
- **Streamlit Web Interface**: User-friendly web application

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. API Key Configuration

The Google API key is already configured in the code:
```python
GOOGLE_API_KEY = "AIzaSyC67N9Gtw95ndsSLiwYT9e6gyVIDiPiL28"
```

### 3. Test the Integration

Before running the main application, test that the Gemini API is working:

```bash
python test_gemini.py
```

## Usage

### Option 1: Streamlit Web Interface

Run the main Streamlit application:

```bash
streamlit run main_gemini.py
```

This will open a web interface where you can:
- Upload PDF documents
- Ask questions about the uploaded documents
- Get AI-generated answers based on the document content

### Option 2: Command Line RAG Pipeline

Use the RAG pipeline directly:

```bash
python rag_pipeline_gemini.py
```

### Option 3: Vector Database Setup

If you want to set up the vector database with your own documents:

```bash
python vector_database_gemini.py
```

## File Structure

- `main_gemini.py` - Main Streamlit application
- `rag_pipeline_gemini.py` - RAG pipeline implementation
- `vector_database_gemini.py` - Vector database setup and management
- `test_gemini.py` - Test script for API integration
- `requirements.txt` - Python dependencies

## How It Works

1. **Document Processing**: PDFs are loaded and split into chunks
2. **Embedding Generation**: Text chunks are converted to vectors using Google's embedding model
3. **Vector Storage**: Embeddings are stored in a FAISS vector database
4. **Query Processing**: User questions are converted to embeddings and used to find relevant document chunks
5. **Answer Generation**: Gemini AI generates answers based on the retrieved context

## Models Used

- **LLM**: `gemini-1.5-pro` - For generating answers
- **Embeddings**: `models/embedding-001` - For text vectorization

## Differences from DeepSeek Version

- Replaced Ollama embeddings with Google's text embedding model
- Replaced DeepSeek LLM with Gemini 1.5 Pro
- Removed dependency on local Ollama installation
- Added Google API key configuration
- Enhanced error handling and user feedback

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure your Google API key is valid and has the necessary permissions
2. **Rate Limiting**: Google API has rate limits; if you hit them, wait and try again
3. **Model Availability**: Ensure the specified Gemini models are available in your region

### Getting Help

- Check the test script output for specific error messages
- Verify your internet connection
- Ensure all dependencies are properly installed

## Security Note

⚠️ **Important**: The API key is hardcoded in this example for demonstration purposes. In production, use environment variables or secure configuration management. 