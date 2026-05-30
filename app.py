import streamlit as st
import os

from src.config import UPLOAD_FOLDER

from src.ingest import (
    build_knowledge_base
)

from src.rag_pipeline import (
    ask_question
)

from src.utils import (
    clear_vector_database,
    format_sources
)

# -----------------------
# PAGE CONFIG
# -----------------------

st.set_page_config(
    page_title="Document Q&A Bot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Document Q&A Bot")
st.markdown(
    "Upload documents, build a knowledge base, and ask questions."
)

# -----------------------
# FILE UPLOAD
# -----------------------

st.sidebar.header("Upload Documents")

uploaded_files = st.sidebar.file_uploader(
    "Choose PDF, DOCX, or TXT files",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if uploaded_files:

    os.makedirs(
        UPLOAD_FOLDER,
        exist_ok=True
    )

    for uploaded_file in uploaded_files:

        file_path = os.path.join(
            UPLOAD_FOLDER,
            uploaded_file.name
        )

        with open(
            file_path,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

    st.sidebar.success(
        f"{len(uploaded_files)} file(s) uploaded."
    )

# -----------------------
# BUILD KNOWLEDGE BASE
# -----------------------

if st.sidebar.button(
        "Build Knowledge Base"
):

    with st.spinner(
            "Indexing documents..."
    ):

        total_chunks = (
            build_knowledge_base()
        )

    st.sidebar.success(
        f"Knowledge base created with {total_chunks} chunks."
    )

# -----------------------
# CLEAR DATABASE
# -----------------------

if st.sidebar.button(
        "Clear Knowledge Base"
):

    clear_vector_database()

    st.sidebar.success(
        "Knowledge base cleared."
    )

# -----------------------
# QUESTION SECTION
# -----------------------

st.subheader("Ask a Question")

question = st.text_input(
    "Enter your question"
)

if st.button("Ask"):

    if not question:

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
                "Searching..."
        ):

            answer, docs = (
                ask_question(
                    question
                )
            )

        st.subheader("Answer")

        st.write(answer)

        st.subheader("Sources")

        sources = format_sources(
            docs
        )

        for source in sources:

            st.write(
                f"• {source}"
            )

        st.subheader(
            "Retrieved Chunks"
        )

        for i, doc in enumerate(
                docs,
                start=1
        ):

            with st.expander(
                    f"Chunk {i}"
            ):

                st.write(
                    doc.page_content
                )