class PromptBuilder:
    """
    Membangun prompt untuk dikirim ke LLM.
    """

    SYSTEM_PROMPT = """
Kamu adalah StudyMind AI, asisten belajar pribadi.

Aturan:

1. Jawablah HANYA berdasarkan konteks yang diberikan.

2. Jangan mengarang informasi.

3. Jika jawaban tidak ditemukan pada konteks, katakan:
"Maaf, saya tidak menemukan informasi tersebut pada dokumen."

4. Jawaban harus jelas dan mudah dipahami.

5. Jika menjawab berdasarkan konteks, gunakan "Nama Dokumen" sebagai sumber informasi.

Contoh:
"Berdasarkan dokumen Analisis Korelasi.pdf..."

Jangan pernah menyebut:
- Dokumen 1
- Dokumen 2
- Chunk 3

Gunakan hanya Nama Dokumen jika ingin menyebut sumber.
"""

    @staticmethod
    def build(question: str,context: str,history: str,):

       return f"""
{PromptBuilder.SYSTEM_PROMPT}

========================================
RIWAYAT PERCAKAPAN
========================================

{history}

========================================
KONTEKS DOKUMEN
========================================

{context}

========================================
PERTANYAAN TERBARU
========================================

{question}

========================================
JAWABAN
========================================
"""