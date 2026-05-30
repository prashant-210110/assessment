# src/ingest.py

from src.document_loader import (
    load_documents
)

from src.text_chunker import (
    split_documents
)

from src.embedding_model import (
    get_embedding_model
)

from src.vector_store import (
    create_vector_store
)

from src.config import (
    UPLOAD_FOLDER
)


def build_knowledge_base():

    documents = load_documents(
        UPLOAD_FOLDER
    )

    chunks = split_documents(
        documents
    )

    embedding_model = (
        get_embedding_model()
    )

    create_vector_store(
        chunks,
        embedding_model
    )

    return len(chunks)