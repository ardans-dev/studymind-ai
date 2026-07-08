from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from pathlib import Path
import shutil

from app.database.session import get_db
from app.services.document_service import DocumentService
from app.services.document_db_service import DocumentDBService

router = APIRouter()

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)


@router.post("/workspace/{workspace_id}/upload")
async def upload_document(
    workspace_id: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    filepath = UPLOAD_FOLDER / file.filename

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document, chunks = DocumentService.process(str(filepath))

    DocumentDBService.create(
        db=db,
        workspace_id=workspace_id,
        title=document.title,
        path=str(filepath),
        filetype=document.metadata["type"],
        pages=document.metadata.get("pages", 0),
    )

    return {
        "title": document.title,
        "chunks": len(chunks),
        "preview": document.content[:300],
    }