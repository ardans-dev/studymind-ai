import chromadb


class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="chroma")

        self.collection = self.client.get_or_create_collection(
            name="studymind"
        )

    def add_chunk(self, chunk, embedding):
        self.collection.add(
            ids=[str(chunk.id)],
            embeddings=[embedding],
            documents=[chunk.content],
            metadatas=[
                {
                    "title": chunk.title,
                    **chunk.metadata,
                }
            ],
        )

    def count(self):
        return self.collection.count()

    def search(self, embedding, top_k=5):
        result = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )

        return result