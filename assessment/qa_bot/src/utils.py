# src/utils.py

import os
import shutil

from src.config import (
    VECTOR_DB_PATH
)


def clear_vector_database():

    if os.path.exists(
            VECTOR_DB_PATH
    ):
        shutil.rmtree(
            VECTOR_DB_PATH
        )


def format_sources(
        retrieved_docs
):

    sources = []

    for doc in retrieved_docs:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        page = doc.metadata.get(
            "page",
            "N/A"
        )

        sources.append(
            f"{source} | Page {page}"
        )

    return list(set(sources))