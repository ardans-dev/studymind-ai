class PromptBuilder:
    """
    Membangun prompt untuk dikirim ke LLM.
    """

    SYSTEM_PROMPT = """
Kamu adalah StudyMind AI, asisten belajar pribadi.

Aturan:
1. Jawablah HANYA berdasarkan konteks yang diberikan.
2. Jangan mengarang jawaban.
3. Jika informasi tidak ditemukan pada konteks, katakan:
   "Maaf, saya tidak menemukan informasi tersebut pada dokumen."
4. Jawaban harus jelas, ringkas, dan mudah dipahami mahasiswa.
"""

    @staticmethod
    def build(question: str, context: str) -> str:

        return f"""
{PromptBuilder.SYSTEM_PROMPT}

========================
KONTEKS
========================

{context}

========================
PERTANYAAN
========================

{question}

========================
JAWABAN
========================
"""
