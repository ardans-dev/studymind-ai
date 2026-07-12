from datetime import datetime

from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: str
    title: str
    type: str
    pages: int
    chunks: int
    uploaded_at: datetime