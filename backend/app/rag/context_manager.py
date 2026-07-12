from app.core.config import settings

class ContextManager:
    """
    Mengelola context yang akan dikirim ke LLM.

    Tujuan:
    - Membatasi jumlah context.
    - Menjaga urutan context.
    - Menjadi satu pintu untuk seluruh fitur AI.
    """

    @staticmethod
    def prepare(documents: list[str]) -> list[str]:

        if not documents:
            return []

        return documents[: settings.MAX_CONTEXT_DOCUMENTS]