import fitz

from app.models.document import Document
from app.parsers.base import BaseParser
from app.rag.cleaner import DocumentCleaner


class PDFParser(BaseParser):
    def parse(self, filepath: str) -> Document:
        pdf = fitz.open(filepath)

        text = ""

        for page in pdf:
            text += page.get_text()

        cleaned = DocumentCleaner.clean(text)

        document = Document(
            title=filepath.split("/")[-1],
            content=cleaned,
            metadata={
                "pages": len(pdf),
                "type": "pdf",
            },
        )

        pdf.close()

        return document
