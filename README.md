# Agentic AI Assistant

An Agentic AI Assistant built using FastAPI, Ollama, and a local Large Language Model (LLM).

## Project Overview

This project demonstrates an AI agent capable of understanding user requests, deciding whether a tool is required, executing the selected tool, and generating a final response.

The system uses a locally running LLM through Ollama.

## Architecture

User
↓
Frontend
↓
FastAPI Backend
↓
Agent Controller
↓
Planner
↓
Tool Selection
├── Calculator
├── Web Search
├── File Reader
└── None
↓
Executor
↓
Tool Result
↓
Local LLM
↓
Final Response
↓
Memory
↓
Frontend

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Ollama
- Local LLM
- HTML
- CSS
- JavaScript
- Requests
- BeautifulSoup
- Pydantic
- JSON

## Available Tools

### Calculator

Performs mathematical calculations safely without using Python's unsafe `eval()` function.

### Web Search

Searches the web when the agent determines that external or current information is required.

### File Reader

Reads text files from the project's `data` directory.

### Memory

Stores recent user and assistant messages in a JSON file.

## Project Structure

```text
agentic-ai-project/
│
├── backend/
│   ├── main.py
│   ├── agent/
│   ├── tools/
│   ├── models/
│   ├── schemas/
│   └── config.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data/
│   └── memory.json
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md