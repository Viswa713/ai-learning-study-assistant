from backend.models.llm import generate_response
from backend.rag.retriever import retrieve


def generate_quiz(
    course_material: str,
    number_of_questions: int = 5,
    difficulty: str = "medium"
):
    """
    Generate a quiz using retrieved course material.
    """

    results = retrieve(
        course_material,
        top_k=5
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

Create an exam-preparation quiz using ONLY
the provided course material.

Course material:
{context}

Topic requested:
{course_material}

Number of questions:
{number_of_questions}

Difficulty:
{difficulty}

For every question provide:

Question:
A.
B.
C.
D.

Correct Answer:
Explanation:

Rules:

- Use only information from the course material.
- Do not invent facts.
- Avoid duplicate questions.
- Make the questions useful for exam preparation.
- Keep explanations clear and concise.
"""

    return generate_response(prompt)