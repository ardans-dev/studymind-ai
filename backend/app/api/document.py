from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.document_db_service import DocumentDBService
from app.schemas.document import DocumentResponse

router = APIRouter(
    prefix="/document",
    tags=["Document"],
)


@router.get(
    "/{workspace_id}",
    response_model=list[DocumentResponse],
)
def list_document(
    workspace_id: str,
    db: Session = Depends(get_db),
):
    return DocumentDBService.list(
        db,
        workspace_id,
    )

@router.delete("/{document_id}")
def delete_document(
    document_id: str,
    db: Session = Depends(get_db),
):

    document = DocumentDBService.delete(
        db,
        document_id,
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return {
        "message": "Document deleted successfully",
    }
