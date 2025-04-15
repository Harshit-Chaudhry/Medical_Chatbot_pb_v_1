import pdfplumber
import pytesseract
from PIL import Image
import os
import sys

try:
    import fitz  
    PYMUPDF_AVAILABLE = True
except ImportError:
    PYMUPDF_AVAILABLE = False

class DocumentProcessor:
    def __init__(self):
        
        if sys.platform == 'win32':
            tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            if os.path.exists(tesseract_path):
                pytesseract.pytesseract.tesseract_cmd = tesseract_path
    
    def extract_text_from_pdf(self, pdf_path):
        """Extract text from PDF file"""
        try:
            text = ""
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
            return text
        except Exception as e:
            return f"Error extracting text from PDF: {str(e)}"
    
    def extract_text_from_image(self, image_path):
        """Extract text from image using OCR"""
        try:
            
            try:
                pytesseract.get_tesseract_version()
            except Exception:
                return "Tesseract OCR is not installed. Please install Tesseract OCR to enable image text extraction."
            
            
            image = Image.open(image_path)
            
            
            text = pytesseract.image_to_string(image)
            return text
        except Exception as e:
            return f"Error extracting text from image: {str(e)}"
    
    def process_document(self, file_path):
        """Process document based on file type"""
        file_extension = os.path.splitext(file_path)[1].lower()
        
        if file_extension == '.pdf':
            return self.extract_text_from_pdf(file_path)
        elif file_extension in ['.jpg', '.jpeg', '.png']:
            return self.extract_text_from_image(file_path)
        else:
            return "Unsupported file format. Please upload a PDF or image file."
    
    def extract_images_from_pdf(self, pdf_path, output_dir):
        """Extract images from PDF file"""
        if not PYMUPDF_AVAILABLE:
            return "PyMuPDF is not installed. Please install it to enable image extraction from PDFs."
            
        try:
            
            os.makedirs(output_dir, exist_ok=True)
            
            
            pdf_document = fitz.open(pdf_path)
            
            
            image_paths = []
            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]
                image_list = page.get_images()
                
                for img_index, img in enumerate(image_list):
                    xref = img[0]
                    base_image = pdf_document.extract_image(xref)
                    image_bytes = base_image["image"]
                    
                    
                    image_path = os.path.join(output_dir, f"page_{page_num + 1}_img_{img_index + 1}.png")
                    with open(image_path, "wb") as img_file:
                        img_file.write(image_bytes)
                    image_paths.append(image_path)
            
            return image_paths
        except Exception as e:
            return f"Error extracting images from PDF: {str(e)}" 