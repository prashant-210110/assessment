from langchain_ollama import OllamaEmbeddings

from src.config import EMBED_MODEL


def get_embedding_model():
    """
    Returns the Ollama embedding model.
    """

    embedding_model = OllamaEmbeddings(
        model=EMBED_MODEL
    )

    return embedding_model