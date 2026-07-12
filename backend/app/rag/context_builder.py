from app.core.config import settings


class ContextBuilder:
    """
    Mengubah hasil retrieval menjadi context
    yang siap dikirim ke LLM dengan batas
    jumlah karakter.
    """

    @staticmethod
    def build(chunks):

        contexts = []

        total_chars = 0

        for chunk in chunks:

            if chunk.score < settings.MIN_SCORE:
                continue

            title = chunk.metadata.get(
                "title",
                "Unknown",
            )

            section = f"""
========================================
Nama Dokumen: {title}

{chunk.content}
"""

            if (
                total_chars + len(section)
                > settings.MAX_CONTEXT_CHARS
            ):
                break

            contexts.append(section)

            total_chars += len(section)

        return "\n".join(contexts)