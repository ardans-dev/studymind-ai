from app.models.chunk import Chunk

from app.rag.vector_store import VectorStore

store = VectorStore()

chunk = Chunk(
    id="1",
    title="Machine Learning",
    content="Machine Learning adalah cabang AI.",
    metadata={"type": "pdf"},
)

store.add_document(
    chunk_id=chunk.id,
    text=chunk.content,
    metadata=chunk.metadata,
)

print("Berhasil disimpan ke Chroma!")
