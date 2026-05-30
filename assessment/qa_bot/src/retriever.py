# src/retriever.py

from src.embedding_model import (
    get_embedding_model
)

from src.vector_store import (
    load_vector_store
)

from src.config import TOP_K


def retrieve_chunks(question):

    embedding_model = (
        get_embedding_model()
    )

    vectordb = load_vector_store(
        embedding_model
    )

    results = vectordb.similarity_search(
        question,
        k=TOP_K
    )

    return results