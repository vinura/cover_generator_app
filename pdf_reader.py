# from langchain.document_loaders import PyPDFLoader 

# def load_pdf(pdf_path):
#     loader = PyPDFLoader(pdf_path)
#     pages = loader.load()
#     return pages

from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from splitter import text_to_doc_splitter

def load_pdf(pdf):
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    document = text_to_doc_splitter(text)
    return document