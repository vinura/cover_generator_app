from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter


def split_text_documents(docs: list):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    documents = text_splitter.split_documents(docs)
    return documents


def text_to_doc_splitter(text: str):
    spliiter = RecursiveCharacterTextSplitter(chunk_size = 10000, chunk_overlap  = 0, length_function = len, add_start_index = True,)
    document = spliiter.create_documents([text])
    return document