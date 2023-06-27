from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os
from pdf_reader import load_pdf
from read_job_posting import extract_text_from_url
from splitter import split_text_documents


def get_cover_letter(url, pdf, openai_api_key):

    pdf_doc = load_pdf(pdf)
    job_post = extract_text_from_url(url)

    pdf_doc.extend(job_post)
    documents = split_text_documents(pdf_doc)

    vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings(openai_api_key = openai_api_key))

    pdf_qa = RetrievalQA.from_chain_type(
        ChatOpenAI(temperature=0.7, model_name='gpt-3.5-turbo', openai_api_key = openai_api_key),
        retriever=vectordb.as_retriever(search_kwargs={'k': 6}),
        chain_type="stuff",
    )

    query = 'Write a cover letter for given CV and Job posting in a conversational style and fill out the writers name in the end using cv'

    result = pdf_qa.run(query)

    return result