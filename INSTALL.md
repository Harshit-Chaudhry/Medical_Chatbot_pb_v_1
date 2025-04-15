# Installation Guide

## Prerequisites

1. Python 3.8 or higher
2. Tesseract OCR (for image text extraction)
3. API Keys:
   - Google Gemini API key
   - Google Maps API key

## Windows Installation

1. Install Python:
   - Download and install Python from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation

2. Install Tesseract OCR:
   - Download the installer from [UB Mannheim Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
   - Run the installer
   - Add Tesseract to your system PATH:
     - Open System Properties > Advanced > Environment Variables
     - Add `C:\Program Files\Tesseract-OCR` to the Path variable

3. Set up the project:
   ```bash
   # Clone the repository
   git clone https://github.com/Harshit-Chaudhry/Medical_Chatbot_pb_v_1.git
   cd Medical_Chatbot_pb_v_1

   # Create and activate virtual environment
   python -m venv .venv
   .venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt

   # Run setup script
   python setup.py
   ```

4. Configure API keys:
   - Open the `.env` file
   - Add your Gemini API key and Google Maps API key
   - Save the file

## Linux/Mac Installation

1. Install Python and required system packages:
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3 python3-pip tesseract-ocr

   # MacOS
   brew install python tesseract
   ```

2. Set up the project:
   ```bash
   # Clone the repository
   git clone <repository-url>
   cd Medical_Chatbot

   # Create and activate virtual environment
   python3 -m venv .venv
   source .venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt

   # Run setup script
   python setup.py
   ```

3. Configure API keys:
   - Open the `.env` file
   - Add your Gemini API key and Google Maps API key
   - Save the file

## Running the Application

1. Activate the virtual environment:
   ```bash
   # Windows
   .venv\Scripts\activate

   # Linux/Mac
   source .venv/bin/activate
   ```

2. Start the application:
   ```bash
   streamlit run app.py
   ```

3. Open your web browser and navigate to:
   ```
   http://localhost:8501
   ```

## Troubleshooting

1. **Tesseract OCR not found**:
   - Make sure Tesseract is installed and added to PATH
   - On Windows, verify the installation path is correct
   - Restart your terminal/command prompt after installation

2. **API Key Errors**:
   - Verify your API keys in the `.env` file
   - Make sure the keys are active and have the required permissions

3. **Dependency Installation Issues**:
   - Try upgrading pip: `pip install --upgrade pip`
   - Make sure you have the latest version of Python
   - On Windows, you might need to install Visual C++ Build Tools

4. **Voice Assistant Issues**:
   - Make sure your microphone is properly connected and configured
   - Check if the required audio drivers are installed

## Support

If you encounter any issues during installation or while using the application, please:
1. Check the troubleshooting section above
2. Search for similar issues in the project's issue tracker
3. Create a new issue with detailed information about the problem 
