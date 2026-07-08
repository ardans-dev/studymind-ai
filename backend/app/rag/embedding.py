from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Mengubah teks menjadi embedding vector menggunakan
    SentenceTransformer.
    """

    _model = None

    @classmethod
    def get_model(cls):
        """
        Load model hanya sekali (Singleton).
        """
        if cls._model is None:
            print("Loading embedding model...")
            cls._model = SentenceTransformer(
                "all-MiniLM-L6-v2"
            )

        return cls._model

    @classmethod
    def encode(cls, text: str) -> list[float]:
        """
        Encode satu teks menjadi vector.
        """
        model = cls.get_model()

        embedding = model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    @classmethod
    def encode_batch(cls, texts: list[str]) -> list[list[float]]:
        """
        Encode banyak teks sekaligus.
        """
        model = cls.get_model()

        embeddings = model.encode(
            texts,
            normalize_embeddings=True,
        )

        return embeddings.tolist()