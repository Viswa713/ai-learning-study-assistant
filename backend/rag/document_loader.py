from pathlib import Path

from pypdf import PdfReader


COURSE_MATERIALS_DIRECTORY = (
    Path(__file__).resolve().parent.parent.parent
    / "data"
    / "course_materials"
)


def load_pdf(filename: str):
    """
    Extract text from a course PDF.
    """

    file_path = (
        COURSE_MATERIALS_DIRECTORY / filename
    ).resolve()

    base_directory = (
        COURSE_MATERIALS_DIRECTORY.resolve()
    )

    if file_path.parent != base_directory:
        return {
            "success": False,
            "error": "Access to this file is not allowed."
        }

    if not file_path.exists():
        return {
            "success": False,
            "error": f"File '{filename}' not found."
        }

    if file_path.suffix.lower() != ".pdf":
        return {
            "success": False,
            "error": "Only PDF files are supported."
        }

    try:
        reader = PdfReader(str(file_path))

        pages = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                pages.append(text)

        content = "\n\n".join(pages).strip()

        return {
            "success": True,
            "filename": filename,
            "pages": len(reader.pages),
            "content": content
        }

    except Exception as error:
        return {
            "success": False,
            "error": str(error)
        }