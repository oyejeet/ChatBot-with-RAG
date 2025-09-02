#!/bin/bash

echo "🚀 Setting up Gemini RAG System..."
echo "=================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv gemini_venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source gemini_venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements_gemini.txt

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "To activate the virtual environment:"
echo "  source gemini_venv/bin/activate"
echo ""
echo "To test the system:"
echo "  python test_gemini.py"
echo ""
echo "To run the demo:"
echo "  python demo_gemini.py"
echo ""
echo "To run the web app:"
echo "  streamlit run main_gemini.py"
echo ""
echo "To deactivate the virtual environment:"
echo "  deactivate" 