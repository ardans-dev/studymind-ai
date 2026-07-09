from app.rag.retriever import Retriever
from app.rag.context_builder import ContextBuilder
from app.rag.prompt_builder import PromptBuilder
from app.rag.llm import LLM


class ChatService:
    @staticmethod
    def ask(
        workspace_id: str,
        question: str,
    ):

        chunks = Retriever.search(
            workspace_id=workspace_id,
            query=question,
        )

        context = ContextBuilder.build(chunks)

        prompt = PromptBuilder.build(
            question=question,
            context=context,
        )

        answer = LLM.chat(prompt)

        sources = []

        for item in chunks:

            sources.append(
                {
                    "title": item.metadata.get("title"),
                    "type": item.metadata.get("type"),
                    "pages": item.metadata.get("pages"),
                    "chunk_index": item.metadata.get("chunk_index"),
                    "score": item.score,
                }
            )

        return {
            "answer": answer,
            "sources": sources,
        }