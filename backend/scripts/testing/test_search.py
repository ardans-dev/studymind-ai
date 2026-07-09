from app.rag.vector_store import VectorStore

store = VectorStore()

result = store.search("Apa itu himpunan?")

print(result)
