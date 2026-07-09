import chromadb

client = chromadb.PersistentClient(path="chroma")

print(client.list_collections())
