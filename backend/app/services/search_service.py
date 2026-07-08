from app.rag.embedding import EmbeddingService
from app.rag.vector_store import VectorStore


class SearchService:

    def __init__(self):
        self.vector_store = VectorStore()

    def search(self, question: str):

        embedding = EmbeddingService.embed(question)

        result = self.vector_store.search(
            embedding=embedding,
            top_k=5,
        )

        return result