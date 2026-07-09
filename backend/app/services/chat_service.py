from app.rag.retriever import Retriever
from app.rag.context_builder import ContextBuilder
from app.rag.prompt_builder import PromptBuilder
from app.rag.llm import LLM
from app.memory.conversation_store import ConversationStore
from app.models.message import Message
from app.rag.history_builder import HistoryBuilder
from app.repositories.conversation_repository import ConversationRepository
from app.database.conversation_model import ConversationDB


class ChatService:
    @staticmethod
    def ask(
        workspace_id: str,
        question: str,
    ):
        
        messages = ConversationStore.get_messages(
            workspace_id
        )

        history = HistoryBuilder.build(
            messages
        )

        chunks = Retriever.search(
            workspace_id=workspace_id,
            query=question,
        )

        context = ContextBuilder.build(chunks)

        prompt = PromptBuilder.build(
            question=question,
            context=context,
            history=history,
        )

        ConversationStore.add_message(
            workspace_id,
            Message(
                role="user",
                content=question,
            ),
        )

        ConversationRepository.save(
            ConversationDB(
                workspace_id=workspace_id,
                role="user",
                content=question,
            )
        )

        answer = LLM.chat(prompt)

        ConversationStore.add_message(
            workspace_id,
            Message(
                role="assistant",
                content=answer,
            ),
        )

        ConversationRepository.save(
            ConversationDB(
                workspace_id=workspace_id,
                role="assistant",
                content=answer,
            )
        )

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