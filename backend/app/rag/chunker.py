from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings
from app.models.chunk import Chunk
from app.models.document import Document


class SemanticChunker:
    """
    Memecah dokumen menjadi beberapa chunk
    menggunakan RecursiveCharacterTextSplitter.
    """

    @staticmethod
    def split(document: Document) -> list[Chunk]:

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
        )

        texts = splitter.split_text(
            document.content
        )

        chunks = []

        for index, text in enumerate(
            texts,
            start=1,
        ):

            metadata = document.metadata.copy()

            metadata["title"] = document.title
            metadata["chunk_index"] = index

            chunks.append(
                Chunk(
                    id=index,
                    title=document.title,
                    content=text,
                    metadata=metadata,
                )
            )

        return chunks