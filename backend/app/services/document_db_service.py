from sqlalchemy.orm import Session

from app.rag.vector_store import VectorStore
from app.repositories.document_repository import DocumentRepository


class DocumentDBService:
    @staticmethod
    def create(
        db: Session,
        workspace_id: str,
        title: str,
        path: str,
        filetype: str,
        pages: int,
        chunks: int,
    ):
        return DocumentRepository.create(
            db,
            workspace_id,
            title,
            path,
            filetype,
            pages,
            chunks,
        )

    @staticmethod
    def list(
        db: Session,
        workspace_id: str,
    ):
        return DocumentRepository.list_by_workspace(
            db,
            workspace_id,
        )

    @staticmethod
    def get_by_id(
        db: Session,
        document_id: str,
    ):
        return DocumentRepository.get_by_id(
            db,
            document_id,
        )

    @staticmethod
    def delete(
        db: Session,
        document_id: str,
    ):

        document = DocumentRepository.get_by_id(
            db,
            document_id,
        )

        if document is None:
            return None

        vector_store = VectorStore(
            document.workspace_id,
        )

        vector_store.delete_document(
            document.id,
        )

        DocumentRepository.delete(
            db,
            document,
        )

        return document