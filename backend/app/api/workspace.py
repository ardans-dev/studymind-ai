from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.workspace_service import WorkspaceService

router = APIRouter(prefix="/workspace", tags=["Workspace"])


@router.post("")
def create(
    name: str,
    db: Session = Depends(get_db),
):

    return WorkspaceService.create(db, name)


@router.get("")
def list_workspace(
    db: Session = Depends(get_db),
):

    return WorkspaceService.list(db)