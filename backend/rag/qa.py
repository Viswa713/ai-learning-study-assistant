from backend.models.llm import generate_response
from backend.rag.retriever import retrieve


def answer_from_course_material(
    question: str
):
    """
    Answer a student's question using
    relevant course-material chunks.
    """

    results = retrieve(
        question,
        top_k=3
    )

    if not results:
        return (
            "I could not find relevant information "
            "in the uploaded course materials."
        )

    context_parts = []

    for result in results:
        context_parts.append(
            f"Source: {result['filename']}\n"
            f"{result['content']}"
        )

    context = "\n\n---\n\n".join(
        context_parts
    )

    prompt = f"""
You are an AI Learning and Study Assistant.

Answer the student's question using ONLY
the provided course material.

If the answer cannot be found in the
course material, clearly say that it is
not available in the provided material.

Do not invent information.

Course material:
{context}

Student question:
{question}

Give a clear and easy-to-understand answer.
"""

    return generate_response(prompt)