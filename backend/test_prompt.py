from app.rag.retriever import Retriever
from app.rag.context_builder import ContextBuilder
from app.rag.prompt_builder import PromptBuilder

chunks = Retriever.search(workspace_id="AI", query="Apa itu himpunan?")

context = ContextBuilder.build(chunks)

prompt = PromptBuilder.build(
    question="Apa itu himpunan?",
    context=context,
)

print(prompt)
