from langchain_community.embeddings import SentenceTransformerEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

def get_embeddings():
    """
    Returns the embedding model. Defaults to a local sentence-transformer.
    """
    # model_name = "all-MiniLM-L6-v2"
    model_name = "BAAI/bge-small-en-v1.5" # Better performance for research
    return SentenceTransformerEmbeddings(model_name=model_name)

if __name__ == "__main__":
    embeddings = get_embeddings()
    text = "This is a test document."
    query_result = embeddings.embed_query(text)
    print(f"Embedding dimension: {len(query_result)}")
