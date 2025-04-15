import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime, timedelta
import json
import time
from src.chatbot.chatbot import MedicalChatbot
from src.voice.voice_assistant import VoiceAssistant
from src.document.document_processor import DocumentProcessor
from src.location.location_services import LocationServices
from src.utils.utils import save_chat_history, format_timestamp
import glob


# Load environment variables
load_dotenv()

# Function to load chat history
def load_most_recent_chat():
    try:
        chat_file = 'data/chats/chat_history.json'
        if not os.path.exists(chat_file):
            return []
        
        with open(chat_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading chat history: {str(e)}")
        return []

# Configure Streamlit page
st.set_page_config(
    page_title="Medical Chatbot",
    page_icon="🏥",
    layout="wide"
)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = load_most_recent_chat()
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = []
if 'initialized' not in st.session_state:
    st.session_state.initialized = False
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""
if 'last_message_time' not in st.session_state:
    st.session_state.last_message_time = None
if 'message_cooldown' not in st.session_state:
    st.session_state.message_cooldown = 2  # Reduced to 2 seconds cooldown


try:
    if not st.session_state.initialized:
        st.session_state.chatbot = MedicalChatbot()
        st.session_state.voice_assistant = VoiceAssistant()
        st.session_state.document_processor = DocumentProcessor()
        st.session_state.location_services = LocationServices()
        st.session_state.initialized = True
except Exception as e:
    st.error(f"Error initializing components: {str(e)}")
    st.stop()


with st.sidebar:
    st.title("Medical Chatbot")
    st.write("---")
    
    
    mode = st.radio(
        "Select Mode",
        ["Chat", "Lab Report Analysis", "Appointments"]
    )
    
    
    voice_enabled = st.checkbox("Enable Voice Input")
    
    
    user_location = st.text_input("Enter your location (for clinic suggestions)")


st.title("Medical Assistant")


if mode == "Chat":
    st.subheader("Ask your health-related questions")
    
    # Display chat history first
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            st.caption(format_timestamp(message["timestamp"]))
    
    # Initialize the form key in session state if not present
    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False
    
    # Chat input
    with st.form(key='chat_form'):
        user_input = st.text_input("Type your question here", key="chat_input")
        submit_button = st.form_submit_button("Send", type="primary")
        
        if submit_button and user_input.strip():
            st.session_state.form_submitted = True
            st.session_state.last_message = user_input
    
    # Voice input handling
    if voice_enabled:
        col1, col2 = st.columns([1, 5])
        with col1:
            if st.button("🎤", help="Start Voice Input"):
                with st.spinner("Listening..."):
                    voice_input = st.session_state.voice_assistant.listen()
                    if voice_input and voice_input != "PyAudio is not installed. Please install PyAudio to enable voice input.":
                        st.session_state.form_submitted = True
                        st.session_state.last_message = voice_input
    
    # Process the message if form was submitted
    if st.session_state.form_submitted:
        current_time = datetime.now()
        
        # Check cooldown period
        if st.session_state.last_message_time:
            time_since_last_message = (current_time - st.session_state.last_message_time).total_seconds()
            if time_since_last_message < st.session_state.message_cooldown:
                st.warning(f"Please wait {st.session_state.message_cooldown - int(time_since_last_message)} seconds before sending another message.")
                st.session_state.form_submitted = False
                st.rerun()
        
        try:
            # Add user message
            new_message = {
                "role": "user",
                "content": st.session_state.last_message,
                "timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S")
            }
            st.session_state.chat_history.append(new_message)
            
            # Get bot response
            with st.spinner("Thinking..."):
                response = st.session_state.chatbot.get_response(st.session_state.last_message)
                
                if response:
                    # Add bot response
                    bot_message = {
                        "role": "assistant",
                        "content": response,
                        "timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    st.session_state.chat_history.append(bot_message)
                    
                    # Save chat history only once after both messages are added
                    save_chat_history(st.session_state.chat_history)
                    
                    if voice_enabled:
                        st.session_state.voice_assistant.speak(response)
            
            # Update last message time
            st.session_state.last_message_time = current_time
            st.session_state.form_submitted = False
            st.rerun()
            
        except Exception as e:
            st.error(f"Error processing request: {str(e)}")
            st.session_state.form_submitted = False


elif mode == "Lab Report Analysis":
    st.subheader("Upload and Analyze Lab Reports")
    
    uploaded_file = st.file_uploader(
        "Upload your lab report (PDF or Image)",
        type=['pdf', 'png', 'jpg', 'jpeg']
    )
    
    if uploaded_file:
        try:
            
            file_path = os.path.join("data/reports", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            st.session_state.uploaded_files.append({
                "name": uploaded_file.name,
                "path": file_path,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
            st.success(f"File {uploaded_file.name} uploaded successfully!")
            
            
            with st.spinner("Analyzing document..."):
                text = st.session_state.document_processor.process_document(file_path)
                if text:
                    analysis = st.session_state.chatbot.analyze_lab_report(text)
                    st.write("Analysis Results:")
                    st.write(analysis)
        
        except Exception as e:
            st.error(f"Error processing document: {str(e)}")


elif mode == "Appointments":
    st.subheader("Book Appointments")
    
    if user_location:
        st.write(f"Finding clinics near {user_location}")
        with st.spinner("Searching for nearby clinics..."):
            try:
                clinics = st.session_state.location_services.find_nearby_healthcare(user_location)
                if isinstance(clinics, list):
                    for clinic in clinics:
                        with st.expander(f"{clinic['name']} - Rating: {clinic.get('rating', 'N/A')}"):
                            st.write(f"Address: {clinic['address']}")
                            if clinic.get('phone'):
                                st.write(f"Phone: {clinic['phone']}")
                            if clinic.get('website'):
                                st.write(f"Website: {clinic['website']}")
                            if clinic.get('opening_hours'):
                                st.write("Opening Hours:")
                                for hours in clinic['opening_hours']:
                                    st.write(f"- {hours}")
                else:
                    st.error(clinics)
            except Exception as e:
                st.error(f"Error searching for clinics: {str(e)}")
    else:
        st.warning("Please enter your location in the sidebar to find nearby clinics")


st.write("---")
st.caption("Chaudhary Medical Assistant - Powered by Harshit Chaudhary") 