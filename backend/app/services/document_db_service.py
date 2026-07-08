from sqlalchemy.orm import Session

from app.repositories.document_repository import DocumentRepository


class DocumentDBService:

    @staticmethod
    def create(
        db: Session,
        workspace_id,
        title,
        path,
        filetype,
        pages,
    ):
        return DocumentRepository.create(
            db,
            workspace_id,
            title,
            path,
            filetype,
            pages,
        )

    @staticmethod
    def list(db: Session, workspace_id: str):
        return DocumentRepository.list_by_workspace(
            db,
            workspace_id,
        )