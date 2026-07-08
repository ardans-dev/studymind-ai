from app.models.document import Document
from app.rag.chunker import SemanticChunker


class ChunkService:

    @staticmethod
    def create_chunks(document: Document):

        return SemanticChunker.split(document)