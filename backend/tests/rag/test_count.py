import chromadb

client = chromadb.PersistentClient(path="chroma")

for collection in client.list_collections():

    print("=" * 50)

    print("Collection :", collection.name)

    print("Count      :", collection.count())

    print("Peek       :")

    print(collection.peek())