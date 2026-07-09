from dataclasses import dataclass

from app.rag.vector_store import VectorStore


@dataclass
class SearchResult:
    """
    Hasil pencarian semantic search.
    """

    content: str

    score: float

    metadata: dict


class Retriever:
    @staticmethod
    def search(
        workspace_id: str,
        query: str,
        limit: int = 5,
    ) -> list[SearchResult]:

        store = VectorStore(workspace_id)

        result = store.search(
            query=query,
            n_results=limit,
        )

        documents = result.get(
            "documents",
            [[]],
        )[0]

        metadatas = result.get(
            "metadatas",
            [[]],
        )[0]

        distances = result.get(
            "distances",
            [[]],
        )[0]

        output = []

        for doc, meta, distance in zip(
            documents,
            metadatas,
            distances,
        ):
            score = 1 / (1 + distance)

            output.append(
                SearchResult(
                    content=doc,
                    score=round(score, 4),
                    metadata=meta,
                )
            )

        return output
