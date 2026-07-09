from app.rag.retriever import Retriever


class SearchService:

    @staticmethod
    def search(
        workspace_id: str,
        question: str,
    ):
        return Retriever.search(
            workspace_id=workspace_id,
            query=question,
        )