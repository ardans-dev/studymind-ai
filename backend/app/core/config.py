from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Seluruh konfigurasi aplikasi StudyMind AI.
    Nilai akan dibaca dari file .env.
    """

    # ---------- Database ----------
    DATABASE_URL: str

    # ---------- LLM ----------
    LLM_MODEL: str

    # ---------- Embedding ----------
    EMBED_MODEL: str

    # ---------- Retrieval ----------
    TOP_K: int
    MIN_SCORE: float

    SEMANTIC_WEIGHT: float
    BM25_WEIGHT: float
    SEARCH_MULTIPLIER: int
    MIN_SEARCH_RESULT: int

    # ---------- Chunking ----------
    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 150

    # ---------- Conversation ----------
    MAX_HISTORY: int
    MAX_HISTORY_CHARS: int = 1200

    # ---------- Context ----------
    MAX_CONTEXT_CHARS: int = 3000

    # ---------- Summary ----------
    SUMMARY_BATCH_SIZE: int

    # ---------- Chroma ----------
    CHROMA_PATH: str = "chroma"

    # ---------- Upload ----------
    UPLOAD_DIR: str


    MAX_CONTEXT_DOCUMENTS: int

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Mengembalikan singleton Settings agar
    file .env hanya dibaca satu kali.
    """
    return Settings()


settings = get_settings()