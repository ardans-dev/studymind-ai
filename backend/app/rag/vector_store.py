import chromadb
import os
from app.rag.embedding import EmbeddingService


class VectorStore:

    def __init__(self, workspace_id: str):

        self.client = chromadb.PersistentClient(path="chroma")

        self.collection = self.client.get_or_create_collection(
            name=f"documents_{workspace_id}"
        )

        print("Current Directory :", os.getcwd())
        print("Chroma Path :", os.path.abspath("chroma"))

    def add_documents(self, chunks):

        print("=" * 60)
        print("VECTOR STORE")
        print("Jumlah chunk:", len(chunks))

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for chunk in chunks:

            print(chunk.metadata)

            print("Embedding chunk:", chunk.id)

            embedding = EmbeddingService.encode(chunk.content)

            ids.append(str(chunk.id))
            documents.append(chunk.content)
            embeddings.append(embedding)
            metadatas.append(chunk.metadata)

        print("Menyimpan ke Chroma...")

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )

        print("Berhasil disimpan!")

        print("Jumlah vector sekarang:", self.collection.count())

        print("=" * 60)

    def search(self, query: str, n_results: int = 5):

        embedding = EmbeddingService.encode(query)

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results,
        )