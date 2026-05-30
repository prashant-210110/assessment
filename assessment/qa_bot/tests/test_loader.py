# tests/test_loader.py

import os

from src.document_loader import load_documents


def test_load_documents():

    folder = "data/uploaded_docs"

    if not os.path.exists(folder):
        os.makedirs(folder)

    docs = load_documents(folder)

    assert isinstance(docs, list)