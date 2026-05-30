# tests/test_chunker.py

from langchain_core.documents import Document
from src.text_chunker import split_documents


def test_split_documents():

    docs = [
        Document(
            page_content="This is a sample text. " * 200
        )
    ]

    chunks = split_documents(docs)

    assert len(chunks) > 1
    assert chunks is not None