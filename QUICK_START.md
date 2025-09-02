# Quick Start Guide - Gemini RAG System

## 🚀 Get Started in 3 Steps

### Option 1: Automated Setup (Recommended)

**On macOS/Linux:**
```bash
./setup.sh
```

**On Windows:**
```cmd
setup.bat
```

### Option 2: Manual Setup

#### 1. Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv gemini_venv

# Activate it (macOS/Linux)
source gemini_venv/bin/activate

# Activate it (Windows)
gemini_venv\Scripts\activate.bat
```

#### 2. Install Dependencies
```bash
pip install -r requirements_gemini.txt
```

#### 3. Test the System
```bash
python test_gemini.py
```

#### 4. Run the Application
```bash
streamlit run main_gemini.py
```

## 📁 Files Overview

- **`main_gemini.py`** - Main Streamlit web application
- **`config.py`** - Configuration file with API keys and settings
- **`demo_gemini.py`** - Command-line demo script
- **`test_gemini.py`** - Test script for API integration
- **`setup.sh`** - Automated setup script (macOS/Linux)
- **`setup.bat`** - Automated setup script (Windows)
- **`requirements_gemini.txt`** - Python dependencies
- **`README_Gemini.md`** - Detailed documentation

## 🔑 API Key

Your Google API key is already configured in `config.py`:
```python
GOOGLE_API_KEY = "AIzaSyC67N9Gtw95ndsSLiwYT9e6gyVIDiPiL28"
```

## ⚠️ Rate Limiting

Google's free tier has rate limits. If you hit them:
1. Wait a few minutes
2. Try again
3. The system automatically falls back to alternative models

## 🎯 What You Can Do

1. **Upload PDFs** - Legal documents, contracts, etc.
2. **Ask Questions** - Get AI-powered answers based on document content
3. **Semantic Search** - Find relevant information using natural language

## 🆘 Troubleshooting

### Common Issues:
- **API Errors**: Check your internet connection
- **Rate Limits**: Wait and try again
- **Model Issues**: System automatically tries alternative models
- **Import Errors**: Make sure you're in the virtual environment

### Virtual Environment:
```bash
# Check if activated (should see (gemini_venv) in prompt)
which python

# If not activated:
source gemini_venv/bin/activate  # macOS/Linux
# or
gemini_venv\Scripts\activate.bat  # Windows
```

## 🎉 Success!

Once running, you'll have a fully functional AI lawyer RAG system powered by Google's Gemini AI!

### Quick Commands:
```bash
# Test the system
python test_gemini.py

# Run demo
python demo_gemini.py

# Run web app
streamlit run main_gemini.py
``` 