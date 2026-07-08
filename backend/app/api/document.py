from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.document_db_service import DocumentDBService

router = APIRouter(
    prefix="/document",
    tags=["Document"],
)


@router.get("/{workspace_id}")
def list_document(
    workspace_id: str,
    db: Session = Depends(get_db),
):
    return DocumentDBService.list(
        db,
        workspace_id,
    )