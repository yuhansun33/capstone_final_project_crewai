from langchain_chroma import Chroma
from langchain.schema.document import Document
from embedding import get_embedding
import os
import shutil

class ChromaVectorDatabase:
    def __init__(self, persist_directory="./chroma_db"):
        self.persist_directory = persist_directory
        self.vector_database = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=get_embedding(),
        )

    def query_chroma(self, query_text: str, number_of_most_similar_results: int = 5):
        results = self.vector_database.similarity_search_with_score(query_text, k=number_of_most_similar_results)
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        return context_text

    def record_metadata_chunks(self, chunks: list[Document]):
        previous_page_id = None
        current_chunk = 0
        for chunk in chunks:
            file_name = chunk.metadata.get("source")
            page = chunk.metadata.get("page")
            current_page_id = f"{file_name}_{page}"
            current_chunk = current_chunk + 1 if previous_page_id == current_page_id else 0
            chunk_id = f"{current_page_id}_{current_chunk}"
            previous_page_id = current_page_id
            chunk.metadata["id"] = chunk_id
        return chunks

    def chroma_add_chunks(self, chunks: list[Document]):
        chunks_with_metadata = self.record_metadata_chunks(chunks)
        existing_items = self.vector_database.get(include=[])
        existing_ids = set(existing_items["ids"])
        print(f"現在有的檔案數為: {len(existing_ids)}")

        new_chunks = [chunk for chunk in chunks_with_metadata if chunk.metadata["id"] not in existing_ids]
        if len(new_chunks) > 0:
            print(f"新增的檔案數為: {len(new_chunks)}")
            new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
            self.vector_database.add_documents(new_chunks, ids=new_chunk_ids)
            self.vector_database.persist()
        else:
            print("沒有新增的檔案")

    def clean_vector_database(self):
        if os.path.exists(self.persist_directory):
            shutil.rmtree(self.persist_directory)
        print("已清空資料庫")