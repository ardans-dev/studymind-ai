import time

import ollama

from app.core.config import settings
from app.core.logger import logger


class LLM:
    """
    Wrapper untuk berkomunikasi dengan Ollama.
    """

    @staticmethod
    def chat(messages: list[dict]) -> str:

        logger.info("LLM dimulai")

        start = time.perf_counter()

        logger.info(
            f"Model: {settings.LLM_MODEL}"
        )

        total_chars = sum(
            len(message["content"])
            for message in messages
        )

        logger.info(
            f"Total Prompt: {total_chars} karakter"
        )

        response = ollama.chat(
            model=settings.LLM_MODEL,
            messages=messages,
        )

        elapsed = time.perf_counter() - start

        logger.info(
            f"LLM selesai ({elapsed:.2f} detik)"
        )

        return response["message"]["content"]