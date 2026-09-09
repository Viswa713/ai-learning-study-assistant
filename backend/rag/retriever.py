import json
import re
from pathlib import Path


VECTOR_STORE_FILE = (
    Path(__file__).resolve().parent.parent.parent
    / "data"
    / "vector_store"
    / "documents.json"
)


def tokenize(text: str):
    """
    Convert text into simple searchable words.
    """

    return set(
        re.findall(
            r"\b[a-zA-Z0-9]+\b",
            text.lower()
        )
    )


def retrieve(
    query: str,
    top_k: int = 3
):
    """
    Retrieve the most relevant course-material chunks.
    """

    if not query.strip():
        return []

    if not VECTOR_STORE_FILE.exists():
        return []

    try:
        with open(
            VECTOR_STORE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            documents = json.load(file)

    except (OSError, json.JSONDecodeError):
        return []

    query_words = tokenize(query)

    scored_documents = []

    for document in documents:

        content = document.get(
            "content",
            ""
        )

        content_words = tokenize(content)

        score = len(
            query_words.intersection(
                content_words
            )
        )

        if score > 0:
            scored_documents.append(
                {
                    "score": score,
                    "id": document.get("id"),
                    "filename": document.get(
                        "filename"
                    ),
                    "chunk_id": document.get(
                        "chunk_id"
                    ),
                    "content": content
                }
            )

    scored_documents.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return scored_documents[:top_k]