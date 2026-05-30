from src.embedding_model import (
    get_embedding_model
)

from src.vector_store import (
    load_vector_store
)

from src.config import TOP_K


def retrieve_chunks(question):

    embeddings = (
        get_embedding_model()
    )

    vectordb = load_vector_store(
        embeddings
    )

    return vectordb.similarity_search(
        question,
        k=TOP_K
    )