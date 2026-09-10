AI Learning & Study Assistant

An Agentic AI-based learning assistant designed to help students learn from course materials, create personalized study plans, generate quizzes, and get answers using an intelligent tool-based workflow.

Project Overview

The AI Learning & Study Assistant combines Agentic AI, RAG, Memory, Tools, and a Local LLM to provide a personalized study experience.

The system understands a student's request, selects the appropriate action, executes the required tool or workflow, and generates a final response.

Key Features

- Course Q&A – Answers questions using uploaded course materials through RAG.
- Study Planner – Creates personalized study and exam preparation plans.
- Quiz Generator – Generates practice questions from course materials.
- Conversation Memory – Maintains recent conversation context.
- Calculator Tool – Performs mathematical calculations safely.
- Web Search Tool – Retrieves information from the web when required.
- File Reader – Reads supported local project files.
- Agentic Workflow – Planner → Executor → Tool/Workflow → Final Response.

Architecture

                    Student
                       |
                       v
                 Web Frontend
                       |
                       v
                 FastAPI Backend
                       |
                       v
                 Agent Controller
                       |
                 +-----+------+
                 |            |
              Planner       Memory
                 |
                 v
              Executor
                 |
       +---------+---------+---------+
       |         |         |         |
      RAG     Study      Quiz      Tools
     Q&A     Planner   Generator
       |         |         |         |
       +---------+---------+---------+
                       |
                       v
                Local LLM (Ollama)
                       |
                       v
                  Final Response

Project Structure

agentic-ai-project/
│
├── backend/
│   ├── agent/
│   ├── rag/
│   ├── tools/
│   ├── models/
│   ├── schemas/
│   ├── config.py
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data/
│   ├── course_materials/
│   └── vector_store/
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md

Technologies Used

- Python
- FastAPI
- Ollama
- Llama 3.2 3B
- Retrieval-Augmented Generation (RAG)
- Pydantic
- HTML
- CSS
- JavaScript
- PyPDF

How It Works

1. The student enters a request through the web interface.
2. The Agent Planner identifies the required action.
3. The Executor calls the appropriate tool or workflow.
4. RAG retrieves relevant information from uploaded course materials when required.
5. Memory provides recent conversation context.
6. The LLM processes the available information.
7. The assistant returns the final response to the student.

Installation

Clone the repository and install the required dependencies:

pip install -r requirements.txt

Install and run Ollama, then download the required model:

ollama pull llama3.2:3b

Create a ".env" file:

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b
MAX_AGENT_STEPS=5

Running the Project

Start the FastAPI backend:

python -m uvicorn backend.main:app --reload

The API will be available at:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

Open "frontend/index.html" in a browser to use the web interface.

RAG Course Materials

Course PDFs can be placed inside:

data/course_materials/

Index a course document using:

python -m backend.rag.index_documents "filename.pdf"

The generated retrieval data is stored in:

data/vector_store/documents.json

Project Status

The project includes a functional prototype of an Agentic AI Learning & Study Assistant with agent planning, tool execution, conversation memory, RAG-based course Q&A, study planning, quiz generation, and a web interface.

Internship

TNSDC – IBM Internship Program

Project: AI Learning & Study Assistant

Author

Viswanathan S

Developed as part of the TNSDC–IBM Internship Project.
