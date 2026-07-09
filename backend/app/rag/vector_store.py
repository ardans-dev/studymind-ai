import chromadb
from app.rag.embedding import EmbeddingService


class VectorStore:
    def __init__(self, workspace_id: str):

        self.client = chromadb.PersistentClient(path="chroma")

        self.collection = self.client.get_or_create_collection(
            name=f"documents_{workspace_id}"
        )

    def add_documents(self, chunks):

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for chunk in chunks:
            embedding = EmbeddingService.encode(chunk.content)

            ids.append(str(chunk.id))
            documents.append(chunk.content)
            embeddings.append(embedding)
            metadatas.append(chunk.metadata)

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )

    def search(self, query: str, n_results: int = 5):

        embedding = EmbeddingService.encode(query)

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results,
        )
