import ollama


class EmbeddingService:

    MODEL = "nomic-embed-text"

    @staticmethod
    def embed(text: str):

        response = ollama.embed(
            model=EmbeddingService.MODEL,
            input=text,
        )

        return response["embeddings"][0]

    @staticmethod
    def embed_many(texts: list[str]):

        response = ollama.embed(
            model=EmbeddingService.MODEL,
            input=texts,
        )

        return response["embeddings"]