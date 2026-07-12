import chromadb

from app.core.config import settings
from app.rag.embedding import EmbeddingService


class VectorStore:
    """
    Wrapper ChromaDB untuk setiap workspace.
    """

    def __init__(self, workspace_id: str):

        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_PATH,
        )

        self.collection = self.client.get_or_create_collection(
            name=f"documents_{workspace_id}"
        )

    def add_documents(self, chunks):

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for chunk in chunks:

            embedding = EmbeddingService.encode(
                chunk.content
            )

            ids.append(
                f"{chunk.metadata['document_id']}_{chunk.metadata['chunk_index']}"
            )

            documents.append(
                chunk.content
            )

            embeddings.append(
                embedding
            )

            metadatas.append(
                chunk.metadata
            )

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )

    def search(
        self,
        query: str,
        n_results: int | None = None,
    ):

        if n_results is None:
            n_results = settings.TOP_K

        embedding = EmbeddingService.encode(
            query
        )

        return self.collection.query(
            query_embeddings=[
                embedding
            ],
            n_results=n_results,
        )

    def get_all_documents(self):
        """
        Mengambil seluruh dokumen
        pada workspace.
        """

        return self.collection.get(
            include=[
                "documents",
                "metadatas",
            ]
        )

    def delete_document(
        self,
        document_id: str,
    ):

        self.collection.delete(
            where={
                "document_id": document_id,
            }
        )

    def peek(self):

        return self.collection.peek()

    def count(self):

        return self.collection.count()