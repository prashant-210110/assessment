# src/generator.py

from langchain_community.llms import (
    Ollama
)

from src.config import (
    LLM_MODEL
)


def generate_answer(
        question,
        retrieved_docs
):

    context = "\n\n".join(
        [
            doc.page_content
            for doc in retrieved_docs
        ]
    )

    prompt = f"""
You are a document assistant.

Answer ONLY from the provided context.

If the answer is not present,
reply:

"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{question}
"""

    llm = Ollama(
        model=LLM_MODEL
    )

    response = llm.invoke(prompt)

    return response