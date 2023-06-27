from bs4 import BeautifulSoup
import requests
from splitter import text_to_doc_splitter


def extract_text_from_url(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, features="html.parser")
    text = []
    for lines in soup.findAll('div', {'class': 'description__text'}):
        text.append(lines.get_text())
    
    lines = (line.strip() for line in text)
    text = '\n'.join(line for line in lines if line)
    
    document = text_to_doc_splitter(text)

    return document