import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
import time
import sys
import subprocess

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.pyaudio_available = self._check_pyaudio()
        os.makedirs('temp', exist_ok=True)
    
    def _check_pyaudio(self):
        """Check if PyAudio is available"""
        try:
            import pyaudio
            return True
        except ImportError:
            return False
    
    def listen(self):
        """Listen for user's voice input and convert to text"""
        if not self.pyaudio_available:
            return "PyAudio is not installed. Please install PyAudio to enable voice input."
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
                
                print("Processing speech...")
                text = self.recognizer.recognize_google(audio)
                return text
                
        except sr.RequestError as e:
            return f"Could not request results; {str(e)}"
        except sr.UnknownValueError:
            return "Could not understand audio"
        except Exception as e:
            if "pyaudio" in str(e).lower():
                return "PyAudio is not installed. Please install PyAudio to enable voice input."
            return f"Error: {str(e)}"
    
    def speak(self, text):
        """Convert text to speech and play it"""
        try:
            
            temp_file = os.path.join('temp', 'response.mp3')
            
           
            tts = gTTS(text=text, lang='en')
            
            
            tts.save(temp_file)
            
            
            if sys.platform.startswith('win'): 
                os.startfile(temp_file)
            else:
                
                opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
                subprocess.call([opener, temp_file])
            
            
            time.sleep(len(text.split()) * 0.3)
            
            
            try:
                os.remove(None)
            except:
                pass
                
        except Exception as e:
            print(f"Error in text-to-speech: {str(e)}") 