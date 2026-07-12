from dataclasses import dataclass

from app.core.config import settings
from app.core.logger import logger
from app.rag.bm25 import BM25Retriever
from app.rag.vector_store import VectorStore


@dataclass
class SearchResult:
    """
    Hasil pencarian Hybrid Search.
    """

    content: str
    score: float
    semantic_score: float
    bm25_score: float
    metadata: dict


class Retriever:
    """
    Melakukan Hybrid Search menggunakan
    Semantic Search + BM25.
    """

    @staticmethod
    def search(
        workspace_id: str,
        query: str,
        limit: int | None = None,
    ) -> list[SearchResult]:

        if limit is None:
            limit = settings.TOP_K

        logger.info(
            f"Retriever dimulai | Workspace={workspace_id}"
        )

        logger.info(
            f"Query: {query}"
        )

        store = VectorStore(workspace_id)

        result = store.search(
            query=query,
            n_results=max(
                limit * settings.SEARCH_MULTIPLIER,
                settings.MIN_SEARCH_RESULT,
            ),
        )

        documents = result.get("documents", [[]])[0]
        metadatas = result.get("metadatas", [[]])[0]
        distances = result.get("distances", [[]])[0]

        logger.info(
            f"Semantic Search menemukan {len(documents)} chunk"
        )

        if not documents:

            logger.warning(
                "Retriever tidak menemukan dokumen."
            )

            return []

        bm25_scores = BM25Retriever.rank(
            query=query,
            documents=documents,
        )

        logger.info(
            "BM25 selesai dihitung."
        )

        output = []

        for doc, meta, distance, bm25 in zip(
            documents,
            metadatas,
            distances,
            bm25_scores,
        ):

            semantic_score = 1 / (1 + distance)

            final_score = (
                semantic_score * settings.SEMANTIC_WEIGHT
                + bm25 * settings.BM25_WEIGHT
            )

            output.append(
                SearchResult(
                    content=doc,
                    score=round(final_score, 4),
                    semantic_score=round(
                        semantic_score,
                        4,
                    ),
                    bm25_score=round(
                        bm25,
                        4,
                    ),
                    metadata=meta,
                )
            )

        output.sort(
            key=lambda x: x.score,
            reverse=True,
        )

        logger.info(
            f"Hybrid Search selesai | Mengembalikan {limit} chunk"
        )

        return output[:limit]