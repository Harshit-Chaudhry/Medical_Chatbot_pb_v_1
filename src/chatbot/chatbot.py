import google.generativeai as genai
import os
from dotenv import load_dotenv

class MedicalChatbot:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('GEMINI_API_KEY')
        genai.configure(api_key=self.api_key)
        
        
        self.model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")
        
        
        self.system_prompt = """You are a medical assistant chatbot. Your role is to:
        1. Provide general health information and advice
        2. Help users understand medical terms and conditions
        3. Suggest when to seek professional medical help
        4. Never provide definitive diagnoses
        5. Always recommend consulting a healthcare professional for serious concerns
        
        Remember:
        - Be empathetic and clear in your responses
        - Use simple language when explaining medical concepts
        - Always prioritize user safety
        - Maintain patient confidentiality
        - Never replace professional medical advice
        - For headache-related queries, ask about:
          * Duration of headache
          * Intensity of pain
          * Location of pain
          * Associated symptoms
          * Any medications taken
          * Any triggers or patterns
          * Any underlying conditions
        """
    
    def get_response(self, user_input):
        try:
            
            prompt = f"{self.system_prompt}\n\nUser: {user_input}\n\nAssistant:"
            
           
            response = self.model.generate_content(prompt)
            
            
            return response.text
        
        except Exception as e:
            return f"I apologize, but I encountered an error: {str(e)}. Please try again or contact support if the issue persists."
    
    def analyze_lab_report(self, report_text):
        try:
           
            prompt = f"""Analyze the following lab report and provide:
            1. A summary of the key findings
            2. Any values that are outside normal ranges
            3. General interpretation (without diagnosis)
            4. Recommendations for follow-up
            
            Lab Report:
            {report_text}
            """
            
            
            response = self.model.generate_content(prompt)
            return response.text
        
        except Exception as e:
            return f"Error analyzing lab report: {str(e)}" 