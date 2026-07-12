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

        # Parse + Chunk
        document, chunks = DocumentService.process(filepath)

        # Simpan metadata dokumen ke SQLite
        saved_document = DocumentDBService.create(
            db=db,
            workspace_id=workspace_id,
            title=document.title,
            path=filepath,
            filetype=document.metadata["type"],
            pages=document.metadata.get("pages", 0),
            chunks=len(chunks),
        )

        # Tambahkan metadata ke setiap chunk
        for chunk in chunks:
            chunk.metadata["document_id"] = saved_document.id
            chunk.metadata["workspace_id"] = workspace_id

        # Baru simpan ke Chroma
        vector_store = VectorStore(workspace_id)
        vector_store.add_documents(chunks)

        return {
            "document": document,
            "chunks": chunks,
        }
    