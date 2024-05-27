from langchain_community.vectorstores import Chroma
from langchain.schema.document import Document
from langchain.tools import tool
from embedding import get_embedding
import os
import shutil

@tool("查詢與給定文本相似的文件")
def query_chroma(query_text: str, number_of_most_similar_results: int = 5) -> str:
    """
    Args:
        query_text (str): 查詢文本。
        number_of_most_similar_results (int, optional): 要返回的最相似文件的數量。默認為 5。

    Returns:
        str: 包含最相似文件內容的字符串，每個文件之間用 "\n\n---\n\n" 分隔。
    """
    vector_database = Chroma(
        persist_directory="./chroma_db",
        embedding_function=get_embedding(),
    )
    results = vector_database.similarity_search_with_score(
        query_text,
        k=number_of_most_similar_results
    )
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    sources = [doc.metadata.get("id", None) for doc, _score in results]
    context_text = f"來源: {sources}\n\n{context_text}"
    return context_text

def record_metadata_chunks(chunks: list[Document]) -> list[Document]:
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

def chroma_add_chunks(chunks: list[Document]) -> None:
    vector_database = Chroma(
        persist_directory="./chroma_db",
        embedding_function=get_embedding(),
    )
    chunks_with_metadata = record_metadata_chunks(chunks)
    existing_items = vector_database.get(include=[])
    existing_ids = set(existing_items["ids"])
    print(f"現在有的檔案數為: {len(existing_ids)}")
    
    # 只添加新的檔案
    new_chunks = [chunk for chunk in chunks_with_metadata if chunk.metadata["id"] not in existing_ids]
    if len(new_chunks) > 0:
        print(f"新增的檔案數為: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        vector_database.add_documents(new_chunks, ids=new_chunk_ids)
        vector_database.persist()
    else:
        print("沒有新增的檔案")

def clean_vector_database() -> None:
    if os.path.exists("chroma_db"):
        shutil.rmtree("chroma_db")
    print("已清空資料庫")
    
    
if __name__ == "__main__":
    from document_process import DocumentProcessor
    data_path = "data"
    processor = DocumentProcessor(data_path)
    processed_documents = processor.process_documents()
    chroma_add_chunks(processed_documents)  