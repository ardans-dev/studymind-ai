from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.models.document import Document
from app.models.chunk import Chunk


class SemanticChunker:

    @staticmethod
    def split(document: Document):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
        )

        texts = splitter.split_text(document.content)

        chunks = []

        for i, text in enumerate(texts):

            chunks.append(
                Chunk(
                    id=i + 1,
                    title=document.title,
                    content=text,
                    metadata=document.metadata,
                )
            )
            
        return chunks