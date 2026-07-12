from app.rag.vector_store import VectorStore

store = VectorStore("AI")

print("Jumlah Vector :", store.count())
print(store.peek())