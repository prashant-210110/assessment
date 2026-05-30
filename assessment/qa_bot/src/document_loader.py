# src/document_loader.py

import os

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader
)


def load_documents(folder_path):

    documents = []

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        try:

            if file.endswith(".pdf"):

                loader = PyPDFLoader(file_path)
                documents.extend(loader.load())

            elif file.endswith(".docx"):

                loader = Docx2txtLoader(file_path)
                documents.extend(loader.load())

            elif file.endswith(".txt"):

                loader = TextLoader(file_path)
                documents.extend(loader.load())

        except Exception as e:

            print(f"Error loading {file}: {e}")

    return documents