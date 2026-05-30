# src/text_chunker.py

from langchain.text_splitter import RecursiveCharacterTextSplitter

from assessment.qa_bot.src.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    return chunks