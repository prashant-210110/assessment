import os

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader
)


def load_documents(folder_path):

    documents = []

    for file in os.listdir(folder_path):

        path = os.path.join(folder_path, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)

        elif file.endswith(".docx"):
            loader = Docx2txtLoader(path)

        elif file.endswith(".txt"):
            loader = TextLoader(path)

        else:
            continue

        documents.extend(loader.load())

    return documents