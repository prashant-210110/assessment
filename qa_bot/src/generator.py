from langchain_ollama import (
    OllamaLLM
)

from src.config import (
    LLM_MODEL
)


def generate_answer(
        question,
        docs
):

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    prompt = f"""
Answer only from the context.

Context:
{context}

Question:
{question}
"""

    llm = OllamaLLM(
        model=LLM_MODEL
    )

    return llm.invoke(prompt)