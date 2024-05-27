from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

def load_documents(DATA_PATH: str):
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    return document_loader.load()

def spilt_documents(documents: list[Document]):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
    )
    return splitter.split_documents(documents)

if __name__ == "__main__":
    documents = load_documents("data")
    # print(len(documents))
    splitted_documents = spilt_documents(documents)
    # print(splitted_documents)
    