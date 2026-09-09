import os

from dotenv import load_dotenv


load_dotenv()


# Ollama configuration
OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2:3b"
)


# Agent configuration
MAX_AGENT_STEPS = int(
    os.getenv(
        "MAX_AGENT_STEPS",
        "5"
    )
)


# Application configuration
APP_NAME = "AI Learning & Study Assistant"

APP_VERSION = "1.0.0"