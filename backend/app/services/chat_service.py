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

        for chunk in chunks:
            sources.append(
                {
                    "title": chunk.metadata.get("title"),
                    "type": chunk.metadata.get("type"),
                    "pages": chunk.metadata.get("pages"),
                    "chunk_index": chunk.metadata.get("chunk_index"),
                    "score": chunk.score,
                }
            )

        return {
            "answer": answer,
            "chunks": len(chunks),
            "sources": sources,
        }
