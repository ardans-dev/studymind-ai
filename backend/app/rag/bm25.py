from rank_bm25 import BM25Okapi


class BM25Retriever:

    @staticmethod
    def tokenize(text: str) -> list[str]:
        return text.lower().split()

    @staticmethod
    def rank(
        query: str,
        documents: list[str],
    ) -> list[float]:

        if not documents:
            return []

        bm25 = BM25Okapi(
            [
                BM25Retriever.tokenize(doc)
                for doc in documents
            ]
        )

        scores = bm25.get_scores(
            BM25Retriever.tokenize(query)
        )

        max_score = max(scores)

        if max_score == 0:
            return [0.0] * len(scores)

        return [
            score / max_score
            for score in scores
        ]