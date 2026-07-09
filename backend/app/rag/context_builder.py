class ContextBuilder:
    """
    Mengubah hasil retrieval menjadi context
    yang siap dikirim ke LLM.
    """

    @staticmethod
    def build(chunks):

        contexts = []

        for i, chunk in enumerate(chunks, start=1):
            contexts.append(f"""[Dokumen {i}]

{chunk.content}
""")

        return "\n-------------------------\n".join(contexts)
