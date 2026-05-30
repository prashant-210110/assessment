from langchain_ollama import (
    OllamaEmbeddings
)

from src.config import EMBED_MODEL


def get_embedding_model():

    return OllamaEmbeddings(
        model=EMBED_MODEL
    )