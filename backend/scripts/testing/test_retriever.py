from app.rag.retriever import Retriever

results = Retriever.search(
    workspace_id="AI",
    query="Apa itu himpunan?",
)

for item in results:
    print("=" * 50)

    print("Score :", item.score)

    print("Type  :", item.metadata["type"])

    print(item.content[:200])
