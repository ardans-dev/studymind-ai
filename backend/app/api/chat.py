from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat_service import ChatService

router = APIRouter(
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    workspace_id: str
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    return ChatService.ask(
        workspace_id=request.workspace_id,
        question=request.question,
    )