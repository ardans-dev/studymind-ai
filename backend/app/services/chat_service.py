from app.services.search_service import SearchService
from app.rag.prompt_builder import PromptBuilder
from app.rag.llm import LLM


class ChatService:

    @staticmethod
    def ask(
        workspace_id: str,
        question: str,
    ):

        chunks = SearchService.search(
            workspace_id,
            question,
        )

        prompt = PromptBuilder.build(
            question,
            chunks,
        )

        answer = LLM.chat(prompt)

        return {
            "answer": answer,
            "sources": chunks,
        }