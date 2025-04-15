# Medical_Chatbot
=======

A comprehensive healthcare assistant that provides:
- Text-based health queries using Gemini API
- Voice assistant capabilities
- Lab report analysis (PDF/Image upload)
- Appointment booking and clinic suggestions
- User chat history and report storage

## Features

1. **Health Chatbot**
   - Text-based health queries
   - Voice input/output
   - Multi-language support

2. **Lab Report Analysis**
   - PDF and image upload support
   - OCR for text extraction
   - AI-powered analysis using Gemini

3. **Appointment & Clinic Services**
   - Nearby clinic/hospital suggestions
   - Appointment booking system
   - Location-based services

4. **User Management**
   - Chat history storage
   - Report storage
   - Appointment history

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: Streamlit
- **AI/ML**: Google Gemini API
- **Voice**: Web Speech API, gTTS, speech_recognition
- **Document Processing**: pdfplumber, PyMuPDF, pytesseract
- **Location Services**: Google Maps API
- **Database**: Local file storage (JSON/CSV)

## Setup Instructions

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file
   - Add your API keys for Gemini, Maps, etc.

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Project Structure

```
medical_chatbot/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── src/                  # Source code
│   ├── chatbot/          # Chatbot core
│   ├── voice/            # Voice processing
│   ├── document/         # Document processing
│   ├── location/         # Location services
│   └── utils/            # Utility functions
├── data/                 # Data storage
│   ├── chats/           # Chat history
│   ├── reports/         # Uploaded reports
│   └── appointments/    # Appointment records
└── tests/               # Test files
```

## Demo Output

### Chatbot Interaction
Below is an example of the chatbot in action:

![Chatbot Demo](.readmeJunk\1_image.png)

**Example Interaction:**
- **User:** Hey, I have a fever about 101 deg temp. Can you suggest me some medicine or home remedy about it?  
- **Chatbot:** Provides general advice like rest, hydration, fever reducers, and when to seek medical attention.

---

### Medical Report Analysis
The chatbot also supports lab report analysis:

1.![Medical Report Analysis](.readmeJunk\2_image.png)
2.![Medical Report Analysis](.readmeJunk\3_image.png)
**Example Features:**
- Upload lab reports (PDF/Image).
- Extracts key findings like deficiencies and abnormal values.
- Provides recommendations for follow-up actions.

---

### Appointment Booking
The chatbot can suggest nearby clinics and hospitals based on your location:

![Appointment Booking](.readmeJunk\4_image.png)

**Example Features:**
- Location-based clinic suggestions.
- Displays clinic details like ratings, address, and contact information.
- Allows users to book appointments.

---


## License

MIT License

