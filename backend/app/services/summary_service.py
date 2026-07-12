from app.rag.vector_store import VectorStore
from app.rag.context_manager import ContextManager
from app.rag.summarizer import Summarizer


class SummaryService:
    """
    Service untuk membuat ringkasan seluruh dokumen
    dalam satu workspace.
    """

    @staticmethod
    def summarize(workspace_id: str):

        store = VectorStore(workspace_id)

        result = store.get_all_documents()

        documents_db = result.get("documents", [])
        metadatas = result.get("metadatas", [])

        if not documents_db:
            return {
                "summary": "Workspace belum memiliki dokumen."
            }

        documents = []

        for doc, meta in zip(documents_db, metadatas):

            title = meta.get("title", "Unknown")

            documents.append(
                f"""
========================================
Nama Dokumen: {title}

{doc}
"""
            )

        # Semua context AI akan melewati ContextManager
        documents = ContextManager.prepare(documents)

        summary = Summarizer.summarize(documents)

        return {
            "summary": summary,
        }