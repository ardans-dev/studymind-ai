from app.services.search_service import SearchService
from app.rag.prompt_builder import PromptBuilder
from app.rag.llm import LLM


class ChatService:

    def __init__(self):
        self.search = SearchService()

    def ask(self, question: str):

        result = self.search.search(question)

        prompt = PromptBuilder.build(
            question,
            result,
        )

        answer = LLM.chat(prompt)

        return {
            "answer": answer,
            "sources": result["metadatas"][0],
        }