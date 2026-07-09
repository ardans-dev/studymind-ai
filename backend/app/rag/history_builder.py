from app.models.message import Message


class HistoryBuilder:
    """
    Mengubah daftar Message menjadi teks
    yang siap dimasukkan ke prompt.
    """

    @staticmethod
    def build(messages: list[Message]) -> str:

        if not messages:
            return "Belum ada percakapan sebelumnya."

        history = []

        for message in messages:

            role = (
                "User"
                if message.role == "user"
                else "Assistant"
            )

            history.append(
                f"{role}: {message.content}"
            )

        return "\n".join(history)