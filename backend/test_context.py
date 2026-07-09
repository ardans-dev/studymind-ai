from app.rag.retriever import Retriever
from app.rag.context_builder import ContextBuilder

chunks = Retriever.search(

    workspace_id="AI",

    query="Apa itu himpunan?"

)

context = ContextBuilder.build(chunks)

print(context)