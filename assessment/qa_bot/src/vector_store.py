# src/vector_store.py

from langchain_community.vectorstores import (
    Chroma
)

from src.config import VECTOR_DB_PATH


def create_vector_store(
        chunks,
        embedding_model
):

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=VECTOR_DB_PATH
    )

    return vectordb


def load_vector_store(
        embedding_model
):

    vectordb = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embedding_model
    )

    return vectordb