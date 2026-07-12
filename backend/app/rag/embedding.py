from sentence_transformers import SentenceTransformer

from app.core.config import settings
from app.core.logger import logger


class EmbeddingService:
    """
    Service untuk menghasilkan embedding menggunakan
    SentenceTransformer.

    Model hanya dimuat sekali (Singleton).
    """

    _model: SentenceTransformer | None = None

    @classmethod
    def get_model(cls) -> SentenceTransformer:
        """
        Mengembalikan model embedding.
        Model akan dimuat satu kali saat pertama digunakan.
        """

        if cls._model is None:
            logger.info(
                f"Loading embedding model: {settings.EMBED_MODEL}"
            )

            cls._model = SentenceTransformer(
                settings.EMBED_MODEL
            )

            logger.info(
                "Embedding model loaded successfully."
            )

        return cls._model

    @classmethod
    def encode(
        cls,
        text: str,
    ) -> list[float]:
        """
        Encode satu teks menjadi embedding vector.
        """

        embedding = cls.get_model().encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    @classmethod
    def encode_batch(
        cls,
        texts: list[str],
    ) -> list[list[float]]:
        """
        Encode banyak teks menjadi embedding vector.
        """

        embeddings = cls.get_model().encode(
            texts,
            normalize_embeddings=True,
        )

        return embeddings.tolist()