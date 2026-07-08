import chromadb

from app.rag.embedding import EmbeddingService


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="chroma"
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add_document(
        self,
        chunk_id: str,
        text: str,
        metadata: dict,
    ):

        embedding = EmbeddingService.encode(text)

        self.collection.add(

            ids=[chunk_id],

            embeddings=[embedding],

            documents=[text],

            metadatas=[metadata],

        )

    def add_documents(
        self,
        chunks,
    ):

        ids = []

        documents = []

        embeddings = []

        metadatas = []

        for chunk in chunks:

            ids.append(str(chunk.id))

            documents.append(chunk.content)

            embeddings.append(

                EmbeddingService.encode(
                    chunk.content
                )

            )

            metadatas.append(chunk.metadata)

        self.collection.add(

            ids=ids,

            embeddings=embeddings,

            documents=documents,

            metadatas=metadatas,

        )