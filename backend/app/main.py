from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.document import router as document_router
from app.api.summary import router as summary_router
from app.core.logger import logger
from app.rag.embedding import EmbeddingService


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Startup dan shutdown aplikasi.
    """

    logger.info("=" * 60)
    logger.info("StudyMind AI Backend Starting...")
    logger.info("Loading Embedding Model...")

    EmbeddingService.get_model()

    logger.info("Embedding Model Ready.")
    logger.info("=" * 60)

    yield

    logger.info("StudyMind AI Backend Stopped.")


app = FastAPI(
    title="StudyMind AI",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(document_router)
app.include_router(chat_router)
app.include_router(summary_router)