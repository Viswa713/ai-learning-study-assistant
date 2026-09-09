import json
from pathlib import Path


MEMORY_FILE = (
    Path(__file__).resolve().parent.parent.parent
    / "data"
    / "memory.json"
)


def load_memory():
    """
    Load conversation memory from memory.json.
    """

    try:
        if not MEMORY_FILE.exists():
            return []

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (json.JSONDecodeError, OSError):
        return []


def save_memory(memory):
    """
    Save conversation memory to memory.json.
    """

    try:
        with open(
            MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                memory,
                file,
                indent=4,
                ensure_ascii=False
            )

        return True

    except OSError:
        return False


def add_message(role: str, content: str):
    """
    Add a message to conversation memory.
    """

    memory = load_memory()

    memory.append({
        "role": role,
        "content": content
    })

    save_memory(memory)


def get_recent_memory(limit: int = 10):
    """
    Return the most recent messages.
    """

    memory = load_memory()

    return memory[-limit:]