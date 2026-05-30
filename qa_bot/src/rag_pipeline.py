from src.retriever import (
    retrieve_chunks
)

from src.generator import (
    generate_answer
)


def ask_question(question):

    docs = retrieve_chunks(
        question
    )

    answer = generate_answer(
        question,
        docs
    )

    return answer, docs