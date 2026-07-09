import chromadb

client = chromadb.PersistentClient(path="chroma")

collection = client.get_collection("documents_AI")

data = collection.peek(1)

print(data["metadatas"][0])