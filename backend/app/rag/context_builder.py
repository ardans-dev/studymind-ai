class ContextBuilder:
    """
    Mengubah hasil retrieval menjadi context
    yang siap dikirim ke LLM.
    """

    @staticmethod
    def build(chunks):

        contexts = []

        for chunk in chunks:

            title = chunk.metadata.get("title", "Unknown")
            doc_type = chunk.metadata.get("type", "Unknown")
            chunk_index = chunk.metadata.get("chunk_index", "-")

            contexts.append(
                f"""
========================================

Nama Dokumen : {title}
Jenis Dokumen: {doc_type.upper()}
Chunk        : {chunk_index}
Relevansi    : {chunk.score:.3f}

Isi:
{chunk.content}
"""
            )

        return "\n".join(contexts)