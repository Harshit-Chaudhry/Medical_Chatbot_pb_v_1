import os
import json
from datetime import datetime

def save_chat_history(chat_history):
    """Save chat history to file"""
    try:
        # Create chats directory if it doesn't exist
        os.makedirs('data/chats', exist_ok=True)
        
        # Use a fixed filename instead of timestamp-based
        chat_file = 'data/chats/chat_history.json'
        
        # Save to single file
        with open(chat_file, 'w', encoding='utf-8') as f:
            json.dump(chat_history, f, indent=4)
        
        return f"Chat history saved successfully: {chat_file}"
    
    except Exception as e:
        return f"Error saving chat history: {str(e)}"

def load_chat_history(filename):
    """Load chat history from file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        return f"Error loading chat history: {str(e)}"

def format_timestamp(timestamp_str):
    """Format timestamp to readable string"""
    try:
        dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return dt.strftime("%I:%M %p")  # Returns time in 12-hour format
    except:
        return timestamp_str

def validate_file_type(filename, allowed_types):
    """Validate file type"""
    file_extension = os.path.splitext(filename)[1].lower()
    return file_extension in allowed_types

def create_directory_if_not_exists(directory):
    """Create directory if it doesn't exist"""
    try:
        os.makedirs(directory, exist_ok=True)
        return True
    except Exception as e:
        print(f"Error creating directory: {str(e)}")
        return False

def sanitize_filename(filename):
    """Sanitize filename to remove invalid characters"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename 