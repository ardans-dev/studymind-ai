class PromptBuilder:

    @staticmethod
    def build(question: str, search_result):

        documents = search_result["documents"][0]
        metadatas = search_result["metadatas"][0]

        context = ""

        for doc, meta in zip(documents, metadatas):
            title = meta.get("title", "Unknown")

            context += f"""

=== Dokumen : {title} ===

{doc}

"""

        prompt = f"""
Kamu adalah AI Study Assistant.

Jawablah pertanyaan HANYA berdasarkan informasi berikut.

Jika jawabannya tidak ada di dalam konteks, katakan dengan jujur bahwa informasi tidak ditemukan.

============================

{context}

============================

Pertanyaan:

{question}

Jawaban:
"""

        return prompt