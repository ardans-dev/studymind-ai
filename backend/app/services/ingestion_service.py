from app.rag.embedding import EmbeddingService
from app.rag.vector_store import VectorStore


class IngestionService:

    def __init__(self):
        self.vector_store = VectorStore()

    def ingest(self, chunks):

        embeddings = EmbeddingService.embed_many(
            [chunk.content for chunk in chunks]
        )

        for chunk, embedding in zip(chunks, embeddings):
            self.vector_store.add_chunk(
                chunk,
                embedding,
            )

        return self.vector_store.count()