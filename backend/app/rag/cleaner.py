import re


class DocumentCleaner:
    """
    Membersihkan teks hasil parsing.
    """

    @staticmethod
    def clean(text: str) -> str:

        # hapus spasi berlebih
        text = re.sub(r"\s+", " ", text)

        # hapus banyak enter
        text = re.sub(r"\n{2,}", "\n", text)

        return text.strip()