import os
import sys
import subprocess
from setuptools import setup, find_packages

def check_tesseract():
    """Check if Tesseract OCR is installed"""
    try:
        subprocess.run(['tesseract', '--version'], capture_output=True, text=True)
        return True
    except FileNotFoundError:
        return False

def install_tesseract_windows():
    """Provide instructions for installing Tesseract OCR on Windows"""
    print("\nTesseract OCR is required for image text extraction.")
    print("Please download and install Tesseract OCR from:")
    print("https://github.com/UB-Mannheim/tesseract/wiki")
    print("\nAfter installation, add Tesseract to your system PATH or")
    print("set the TESSERACT_CMD environment variable to point to the tesseract executable.")

def check_pymupdf():
    """Check if PyMuPDF is installed"""
    try:
        import fitz
        return True
    except ImportError:
        return False

def install_pymupdf_windows():
    """Provide instructions for installing PyMuPDF on Windows"""
    print("\nPyMuPDF is required for PDF processing.")
    print("Please install Visual C++ Build Tools from:")
    print("https://visualstudio.microsoft.com/visual-cpp-build-tools/")
    print("\nAfter installing Visual C++ Build Tools, run:")
    print("pip install PyMuPDF")

def check_pyaudio():
    """Check if PyAudio is installed"""
    try:
        import pyaudio
        return True
    except ImportError:
        return False

def install_pyaudio_windows():
    """Provide instructions for installing PyAudio on Windows"""
    print("\nPyAudio is required for voice input.")
    print("Please install PyAudio using the following steps:")
    print("1. Download the appropriate wheel file from:")
    print("   https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio")
    print("2. Choose the file matching your Python version and system architecture")
    print("   (e.g., PyAudio‑0.2.14‑cp39‑cp39‑win_amd64.whl for Python 3.9 64-bit)")
    print("3. Install using pip:")
    print("   pip install <downloaded_wheel_file>")

def main():
    # Check for Tesseract OCR
    if not check_tesseract():
        if sys.platform == 'win32':
            install_tesseract_windows()
        else:
            print("\nTesseract OCR is required for image text extraction.")
            print("Please install Tesseract OCR using your package manager.")
    
    # Check for PyMuPDF
    if not check_pymupdf():
        if sys.platform == 'win32':
            install_pymupdf_windows()
        else:
            print("\nPyMuPDF is required for PDF processing.")
            print("Please install it using pip:")
            print("pip install PyMuPDF")
    
    # Check for PyAudio
    if not check_pyaudio():
        if sys.platform == 'win32':
            install_pyaudio_windows()
        else:
            print("\nPyAudio is required for voice input.")
            print("Please install it using your package manager:")
            print("Ubuntu/Debian: sudo apt-get install python3-pyaudio")
            print("MacOS: brew install portaudio && pip install pyaudio")
    
    # Create necessary directories
    os.makedirs('data/chats', exist_ok=True)
    os.makedirs('data/reports', exist_ok=True)
    os.makedirs('data/appointments', exist_ok=True)
    
    # Create .env file if it doesn't exist
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write("""# API Keys
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here

# Application Settings
DEBUG=True
LOG_LEVEL=INFO

# File Storage
MAX_UPLOAD_SIZE=10485760  # 10MB in bytes
ALLOWED_FILE_TYPES=.pdf,.jpg,.jpeg,.png
""")
        print("\nCreated .env file. Please update it with your API keys.")

    print("\nSetup completed successfully!")
    print("\nNext steps:")
    print("1. Install Python dependencies:")
    print("   pip install -r requirements.txt")
    print("2. Update your .env file with API keys")
    print("3. Run the application:")
    print("   streamlit run app.py")

if __name__ == '__main__':
    main() 