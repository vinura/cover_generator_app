import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.chains import RetrievalQA

from pdf_reader import load_pdf
from read_job_posting import extract_text_from_url
from splitter import split_text_documents


def get_cover_letter(url, pdf):

    pdf_doc = load_pdf(pdf)
    job_post = extract_text_from_url(url)

    pdf_doc.extend(job_post)
    documents = split_text_documents(pdf_doc)

    vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings())
    # vectordb.persist() perssit only the CV, otherone dynamic

    # create our Q&A chain
    pdf_qa = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(temperature=0.7, model_name='gpt-3.5-turbo'),
        retriever=vectordb.as_retriever(search_kwargs={'k': 6}),
        return_source_documents=True,
        verbose=False
    )

    query = 'write an overview for upwork Describe my strengths and skills Highlight projects, accomplishments and education using the given CV'
    chat_history = []

    result = pdf_qa({"question": query, "chat_history": chat_history})

    return result["answer"]
