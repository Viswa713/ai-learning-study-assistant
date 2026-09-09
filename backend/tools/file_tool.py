from pathlib import Path


DATA_DIRECTORY = Path(__file__).resolve().parent.parent.parent / "data"


def read_file(filename: str):
    """
    Read a text file from the project's data directory.
    """

    try:
        file_path = DATA_DIRECTORY / filename

        # Prevent access outside the data directory.
        if file_path.parent.resolve() != DATA_DIRECTORY.resolve():
            return {
                "success": False,
                "error": "Access to this file is not allowed."
            }

        if not file_path.exists():
            return {
                "success": False,
                "error": f"File '{filename}' not found."
            }

        if not file_path.is_file():
            return {
                "success": False,
                "error": "The requested path is not a file."
            }

        content = file_path.read_text(
            encoding="utf-8"
        )

        return {
            "success": True,
            "filename": filename,
            "content": content
        }

    except Exception as error:
        return {
            "success": False,
            "error": str(error)
        }