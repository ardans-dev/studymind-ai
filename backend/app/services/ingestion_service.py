from sqlalchemy.orm import Session

from app.rag.vector_store import VectorStore

from app.services.document_service import DocumentService
from app.services.document_db_service import DocumentDBService


class IngestionService:
    @staticmethod
    def ingest(
        db: Session,
        workspace_id: str,
        filepath: str,
    ):

        document, chunks = DocumentService.process(filepath)

        vector_store = VectorStore(workspace_id)

        vector_store.add_documents(chunks)

        DocumentDBService.create(
            db=db,
            workspace_id=workspace_id,
            title=document.title,
            path=filepath,
            filetype=document.metadata["type"],
            pages=document.metadata.get("pages", 0),
        )

        return {
            "document": document,
            "chunks": chunks,
        }
