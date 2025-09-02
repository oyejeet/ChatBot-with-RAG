#!/usr/bin/env python3
"""
Verification script for Gemini RAG System
Run this to verify everything is working correctly
"""

import sys
import os

def check_python_version():
    """Check Python version"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Need Python 3.8+")
        return False

def check_virtual_environment():
    """Check if virtual environment is activated"""
    print("\n🔧 Checking virtual environment...")
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment is activated")
        return True
    else:
        print("❌ Virtual environment is not activated")
        print("   Run: source gemini_venv/bin/activate")
        return False

def check_imports():
    """Check if all required packages can be imported"""
    print("\n📦 Checking package imports...")
    
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
        print("✅ langchain-google-genai imported successfully")
    except ImportError as e:
        print(f"❌ langchain-google-genai import failed: {e}")
        return False
    
    try:
        from langchain_community.document_loaders import PDFPlumberLoader
        print("✅ PDFPlumberLoader imported successfully")
    except ImportError as e:
        print(f"❌ PDFPlumberLoader import failed: {e}")
        return False
    
    try:
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        print("✅ RecursiveCharacterTextSplitter imported successfully")
    except ImportError as e:
        print(f"❌ RecursiveCharacterTextSplitter import failed: {e}")
        return False
    
    try:
        from langchain_community.vectorstores import FAISS
        print("✅ FAISS imported successfully")
    except ImportError as e:
        print(f"❌ FAISS import failed: {e}")
        return False
    
    try:
        import streamlit
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    return True

def check_api_key():
    """Check if API key is configured"""
    print("\n🔑 Checking API key configuration...")
    
    try:
        from config import GOOGLE_API_KEY
        if GOOGLE_API_KEY and len(GOOGLE_API_KEY) > 10:
            print("✅ Google API key is configured")
            return True
        else:
            print("❌ Google API key is empty or too short")
            return False
    except ImportError as e:
        print(f"❌ Could not import config: {e}")
        return False

def check_files():
    """Check if all required files exist"""
    print("\n📁 Checking required files...")
    
    required_files = [
        'main_gemini.py',
        'config.py',
        'demo_gemini.py',
        'test_gemini.py',
        'requirements_gemini.txt',
        'setup.sh',
        'setup.bat'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")
            missing_files.append(file)
    
    return len(missing_files) == 0

def main():
    """Main verification function"""
    print("🔍 Gemini RAG System Verification")
    print("=" * 40)
    
    checks = [
        check_python_version(),
        check_virtual_environment(),
        check_imports(),
        check_api_key(),
        check_files()
    ]
    
    print("\n" + "=" * 40)
    print("📋 Verification Summary")
    print("=" * 40)
    
    passed = sum(checks)
    total = len(checks)
    
    if passed == total:
        print(f"🎉 All {total} checks passed! System is ready to use.")
        print("\n🚀 Next steps:")
        print("   1. Test the system: python test_gemini.py")
        print("   2. Run the demo: python demo_gemini.py")
        print("   3. Start the web app: streamlit run main_gemini.py")
    else:
        print(f"⚠️  {passed}/{total} checks passed. Please fix the issues above.")
        print("\n🔧 Common fixes:")
        print("   - Activate virtual environment: source gemini_venv/bin/activate")
        print("   - Install dependencies: pip install -r requirements_gemini.txt")
        print("   - Check file permissions and paths")

if __name__ == "__main__":
    main() 