from app.core.config import settings
from app.models.message import Message


class HistoryBuilder:
    """
    Mengubah riwayat percakapan menjadi teks
    dengan batas jumlah karakter.
    """

    @staticmethod
    def build(messages: list[Message]) -> str:

        if not messages:
            return "Belum ada percakapan sebelumnya."

        history = []

        total_chars = 0

        for message in reversed(messages):

            role = (
                "User"
                if message.role == "user"
                else "Assistant"
            )

            text = (
                f"{role}: {message.content}"
            )

            # Lewati jika satu pesan saja
            # melebihi batas.
            if len(text) > settings.MAX_HISTORY_CHARS:
                continue

            # Berhenti jika penambahan pesan
            # berikutnya melewati batas.
            if (
                total_chars + len(text)
                > settings.MAX_HISTORY_CHARS
            ):
                break

            history.append(text)

            total_chars += len(text)

        history.reverse()

        if not history:
            return "Belum ada percakapan sebelumnya."

        return "\n".join(history)