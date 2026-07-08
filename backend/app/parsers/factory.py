from pathlib import Path

from app.parsers.pdf_parser import PDFParser


class ParserFactory:

    @staticmethod
    def get(filepath):

        ext = Path(filepath).suffix.lower()

        if ext == ".pdf":
            return PDFParser()

        raise ValueError(f"Unsupported file: {ext}")