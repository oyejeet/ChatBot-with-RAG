@echo off
echo 🚀 Setting up Gemini RAG System...
echo ==================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8+ first.
    pause
    exit /b 1
)

echo ✅ Python found: 
python --version

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv gemini_venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call gemini_venv\Scripts\activate.bat

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo 📚 Installing dependencies...
pip install -r requirements_gemini.txt

echo.
echo 🎉 Setup completed successfully!
echo.
echo To activate the virtual environment:
echo   gemini_venv\Scripts\activate.bat
echo.
echo To test the system:
echo   python test_gemini.py
echo.
echo To run the demo:
echo   python demo_gemini.py
echo.
echo To run the web app:
echo   streamlit run main_gemini.py
echo.
echo To deactivate the virtual environment:
echo   deactivate
echo.
pause 