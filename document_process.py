from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

class DocumentProcessor:
    def __init__(self, data_path: str, chunk_size: int = 1000, chunk_overlap: int = 100):
        self.data_path = data_path
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def load_documents(self):
        document_loader = PyPDFDirectoryLoader(self.data_path)
        return document_loader.load()

    def split_documents(self, documents: list[Document]):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
        )
        return splitter.split_documents(documents)

    def process_documents(self):
        documents = self.load_documents()
        splitted_documents = self.split_documents(documents)
        return splitted_documents
