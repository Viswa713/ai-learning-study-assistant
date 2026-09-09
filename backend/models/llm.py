import requests

from backend.config import OLLAMA_BASE_URL, OLLAMA_MODEL


def generate_response(prompt: str) -> str:
    """
    Send a prompt to the local Ollama model and return its response.
    """

    url = f"{OLLAMA_BASE_URL}/api/generate"

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=300,
        )

        response.raise_for_status()

        data = response.json()

        return data.get("response", "").strip()

    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Make sure Ollama is running."

    except requests.exceptions.Timeout:
        return "Error: Ollama took too long to respond."

    except requests.exceptions.RequestException as error:
        return f"Error communicating with Ollama: {error}"