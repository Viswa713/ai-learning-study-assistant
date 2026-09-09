from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.agent.agent import run_agent
from backend.schemas.request import ChatRequest, ChatResponse
from backend.config import APP_NAME, APP_VERSION


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Agentic AI Assistant is running.",
        "version": APP_VERSION,
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):
    response = run_agent(request.message)

    return ChatResponse(
        response=response
    )