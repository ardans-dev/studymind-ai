from app.rag.llm import LLM
from app.rag.summary_prompt_builder import SummaryPromptBuilder
from app.core.config import settings
from app.core.logger import logger

class Summarizer:
    """
    Melakukan ringkasan dokumen menggunakan
    strategi recursive map-reduce.
    """

    @staticmethod
    def summarize(documents: list[str]) -> str:

        if not documents:
            return "Tidak ada dokumen."

        current_level = documents
        level = 1

        while len(current_level) > 1:

            logger.info(f"========== SUMMARY LEVEL {level} ==========")
            logger.info(f"Input : {len(current_level)} dokumen")

            next_level = []

            for i in range(
                0,
                len(current_level),
                settings.SUMMARY_BATCH_SIZE,
            ):

                batch = current_level[
                    i:i + settings.SUMMARY_BATCH_SIZE
                ]

                context = "\n\n".join(batch)

                prompt = SummaryPromptBuilder.build(
                    context=context,
                )

                try:

                    summary = LLM.chat(prompt)

                    if not summary or not summary.strip():
                        summary = "Ringkasan tidak tersedia."

                except Exception as e:

                    logger.exception(
                        f"Batch {i // settings.SUMMARY_BATCH_SIZE + 1} gagal."
                    )
                    print(e)

                    summary = "Ringkasan tidak tersedia."

                next_level.append(summary)

                logger.info(
                    f"Batch {i // settings.SUMMARY_BATCH_SIZE + 1} selesai."
                )

            logger.info(
                f"Output: {len(next_level)} ringkasan"
            )
            logger.info("====================================")

            current_level = next_level
            level += 1

        logger.info("========== SUMMARY FINISHED ==========")

        return current_level[0]