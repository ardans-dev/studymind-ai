from pathlib import Path
import shutil

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.ingestion_service import IngestionService

router = APIRouter(tags=["Upload"])

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)


@router.post("/workspace/{workspace_id}/upload")
async def upload_document(
    workspace_id: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    """
    Upload dokumen ke workspace.
    """

    filepath = UPLOAD_FOLDER / file.filename

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = IngestionService.ingest(
        db=db,
        workspace_id=workspace_id,
        filepath=str(filepath),
    )

    document = result["document"]
    chunks = result["chunks"]

    return {
        "title": document.title,
        "chunks": len(chunks),
        "preview": document.content[:300],
    }
