from app.models.document import Document
from app.models.chunk import Chunk
from app.parsers.factory import ParserFactory
from app.rag.cleaner import DocumentCleaner
from app.services.chunk_service import ChunkService


class DocumentService:

    @staticmethod
    def parse(filepath: str) -> Document:
        parser = ParserFactory.get(filepath)
        return parser.parse(filepath)

    @staticmethod
    def process(filepath: str) -> tuple[Document, list[Chunk]]:
        document = DocumentService.parse(filepath)

        document.content = DocumentCleaner.clean(document.content)

        chunks = ChunkService.create_chunks(document)

        return document, chunks