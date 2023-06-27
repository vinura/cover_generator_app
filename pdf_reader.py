from PyPDF2 import PdfReader
from splitter import text_to_doc_splitter

def load_pdf(pdf):
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    document = text_to_doc_splitter(text)
    return document