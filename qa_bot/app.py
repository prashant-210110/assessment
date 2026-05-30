import streamlit as st
import os

from src.config import (
    UPLOAD_FOLDER
)

from src.ingest import (
    build_knowledge_base
)

from src.rag_pipeline import (
    ask_question
)

from src.utils import (
    clear_vector_database
)

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

st.title("Document Q&A Bot")

uploaded_files = st.file_uploader(
    "Upload Files",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if uploaded_files:

    for file in uploaded_files:

        save_path = os.path.join(
            UPLOAD_FOLDER,
            file.name
        )

        with open(
            save_path,
            "wb"
        ) as f:

            f.write(
                file.getbuffer()
            )

    st.success(
        "Files uploaded successfully"
    )

if st.button(
        "Build Knowledge Base"
):

    count = build_knowledge_base()

    st.success(
        f"{count} chunks indexed"
    )

question = st.text_input(
    "Ask a Question"
)

if st.button(
        "Ask"
):

    answer, docs = ask_question(
        question
    )

    st.write(answer)

if st.button(
        "Clear Database"
):

    clear_vector_database()

    st.success(
        "Database cleared"
    )