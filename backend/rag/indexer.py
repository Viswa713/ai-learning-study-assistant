import json
from pathlib import Path

from backend.rag.document_loader import load_pdf
from backend.rag.chunker import split_text


VECTOR_STORE_FILE = (
    Path(__file__).resolve().parent.parent.parent
    / "data"
    / "vector_store"
    / "documents.json"
)


def index_document(filename: str):
    """
    Load a course PDF, split it into chunks,
    and store the chunks for retrieval.
    """

    document = load_pdf(filename)

    if not document.get("success"):
        return document

    chunks = split_text(
        document["content"]
    )

    documents = []

    for index, chunk in enumerate(chunks):

        documents.append({
            "id": f"{filename}_{index}",
            "filename": filename,
            "chunk_id": index,
            "content": chunk
        })

    try:
        VECTOR_STORE_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            VECTOR_STORE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                documents,
                file,
                indent=4,
                ensure_ascii=False
            )

        return {
            "success": True,
            "filename": filename,
            "chunks": len(documents)
        }

    except OSError as error:
        return {
            "success": False,
            "error": str(error)
        }