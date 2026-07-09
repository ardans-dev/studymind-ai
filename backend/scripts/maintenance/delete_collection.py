import chromadb

client = chromadb.PersistentClient(path="chroma")

collections = client.list_collections()

print("Collection yang ada:")

for collection in collections:
    print("-", collection.name)

collection_name = input("\nMasukkan nama collection yang ingin dihapus: ")

client.delete_collection(collection_name)

print(f"\nCollection '{collection_name}' berhasil dihapus.")
