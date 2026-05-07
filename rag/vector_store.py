from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import List, Dict, Any
import os

class VectorStoreManager:
    def __init__(self, embeddings):
        self.embeddings = embeddings
        self.vector_store = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            separators=["\n\n", "\n", " ", ""]
        )

    def create_vector_store(self, sections: List[Dict[str, Any]]):
        """
        Creates a FAISS vector store from sections.
        """
        documents = []
        for section in sections:
            chunks = self.text_splitter.split_text(section["content"])
            for chunk in chunks:
                doc = Document(
                    page_content=chunk,
                    metadata={
                        "section": section["section_name"],
                        "page": section["start_page"]
                    }
                )
                documents.append(doc)

        self.vector_store = FAISS.from_documents(documents, self.embeddings)
        return self.vector_store

    def save_vector_store(self, path: str):
        if self.vector_store:
            self.vector_store.save_local(path)

    def load_vector_store(self, path: str):
        self.vector_store = FAISS.load_local(path, self.embeddings, allow_dangerous_deserialization=True)
        return self.vector_store

    def search(self, query: str, k: int = 4) -> List[Document]:
        if not self.vector_store:
            raise ValueError("Vector store not initialized.")
        return self.vector_store.similarity_search(query, k=k)

if __name__ == "__main__":
    # Example usage
    # from embeddings import get_embeddings
    # vsm = VectorStoreManager(get_embeddings())
    # vsm.create_vector_store(sections)
    pass
