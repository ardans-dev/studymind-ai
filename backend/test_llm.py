from app.rag.llm import LLM

answer = LLM.chat(
    """
    Jelaskan analisis korelasi dalam maksimal 3 kalimat.
    """
)

print(answer)