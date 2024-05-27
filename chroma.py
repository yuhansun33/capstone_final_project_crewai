from langchain_chroma import Chroma
from langchain.schema.document import Document
from embedding import get_embedding
import os
import shutil

def record_metadata_chunks(chunks: list[Document]):
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

def chroma_add_chunks(chunks: list[Document]):
    vector_database = Chroma(
        persist_directory="./chroma_db",
        embedding_function=get_embedding(),
    )
    
    chunks_with_metadata = record_metadata_chunks(chunks)
    
    existing_items = vector_database.get(include=[])
    existing_ids = set(existing_items["ids"])
    print(f"現在有的檔案數為: {len(existing_ids)}")
    
    # 有新的檔案才會新增
    new_chunks = [chunk for chunk in chunks_with_metadata if chunk.metadata["id"] not in existing_ids]
    
    if len(new_chunks) > 0:
        print(f"新增的檔案數為: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        vector_database.add_documents(new_chunks, ids=new_chunk_ids)
        vector_database.persist()
    else:
        print("沒有新增的檔案")
        
def clean_vector_database():
    if os.path.exists("chroma_db"):
        shutil.rmtree("chroma_db")
        print("已清空資料庫")
        
if __name__ == "__main__":
    from document_process import load_documents
    from document_process import spilt_documents
    
    documents = load_documents("data")
    chunks = spilt_documents(documents)
    chroma_add_chunks(chunks)
    