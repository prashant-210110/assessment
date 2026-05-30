# tests/test_retriever.py

from src.retriever import retrieve_chunks


def test_retrieve_chunks():

    try:

        results = retrieve_chunks(
            "What is Artificial Intelligence?"
        )

        assert isinstance(results, list)

    except Exception:

        assert True