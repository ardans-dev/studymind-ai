from sqlalchemy.orm import Session

from app.database.document_model import DocumentDB


class DocumentRepository:

    @staticmethod
    def create(
        db: Session,
        workspace_id: str,
        title: str,
        path: str,
        filetype: str,
        pages: int,
    ):

        doc = DocumentDB(
            workspace_id=workspace_id,
            title=title,
            path=path,
            type=filetype,
            pages=pages,
        )

        db.add(doc)
        db.commit()
        db.refresh(doc)

        return doc

    @staticmethod
    def list_by_workspace(
        db: Session,
        workspace_id: str,
    ):
        return (
            db.query(DocumentDB)
            .filter(DocumentDB.workspace_id == workspace_id)
            .all()
        )