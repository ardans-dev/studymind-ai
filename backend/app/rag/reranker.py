from collections import defaultdict


class Reranker:
    """
    Mengelompokkan hasil retrieval berdasarkan dokumen,
    kemudian mengurutkan chunk di dalam dokumen.
    """

    @staticmethod
    def rerank(chunks):

        grouped = defaultdict(list)

        for chunk in chunks:

            document_id = chunk.metadata.get(
                "document_id"
            )

            grouped[document_id].append(
                chunk
            )

        document_scores = []

        for document_id, items in grouped.items():

            average_score = sum(
                item.score for item in items
            ) / len(items)

            document_scores.append(
                (
                    document_id,
                    average_score,
                )
            )

        document_scores.sort(
            key=lambda x: x[1],
            reverse=True,
        )

        ordered = []

        for document_id, _ in document_scores:

            items = grouped[document_id]

            items.sort(
                key=lambda x: x.metadata.get(
                    "chunk_index",
                    0,
                )
            )

            ordered.extend(
                items
            )

        return ordered