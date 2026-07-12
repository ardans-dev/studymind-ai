from app.core.logger import logger
from app.core.profiler import Profiler
from app.database.conversation_model import ConversationDB
from app.memory.conversation_store import ConversationStore
from app.models.message import Message
from app.rag.context_builder import ContextBuilder
from app.rag.history_builder import HistoryBuilder
from app.rag.llm import LLM
from app.rag.prompt_builder import PromptBuilder
from app.rag.reranker import Reranker
from app.rag.retriever import Retriever
from app.repositories.conversation_repository import ConversationRepository


class ChatService:
    @staticmethod
    def ask(
        workspace_id: str,
        question: str,
    ):

        profiler = Profiler()

        logger.info("=" * 60)
        logger.info("REQUEST CHAT")
        logger.info(f"Workspace : {workspace_id}")
        logger.info(f"Question  : {question}")
        logger.info("=" * 60)

        # ---------- History ----------

        messages_history = ConversationStore.get_messages(
            workspace_id
        )

        history = HistoryBuilder.build(
            messages_history
        )

        profiler.checkpoint(
            "History Builder"
        )

        # ---------- Retrieval ----------

        chunks = Retriever.search(
            workspace_id=workspace_id,
            query=question,
        )

        profiler.checkpoint(
            "Retriever"
        )

        # ---------- Reranker ----------

        chunks = Reranker.rerank(
            chunks
        )

        profiler.checkpoint(
            "Reranker"
        )

        # ---------- Context ----------

        context = ContextBuilder.build(
            chunks
        )

        profiler.checkpoint(
            "Context Builder"
        )

        # ---------- Prompt ----------

        llm_messages = PromptBuilder.build(
            question=question,
            context=context,
            history=history,
        )

        profiler.checkpoint(
            "Prompt Builder"
        )

        total_prompt = sum(
            len(item["content"])
            for item in llm_messages
        )

        logger.info(
            f"History : {len(history)} karakter"
        )

        logger.info(
            f"Context : {len(context)} karakter"
        )

        logger.info(
            f"Prompt  : {total_prompt} karakter"
        )

        # ---------- Simpan User ----------

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

        # ---------- LLM ----------

        answer = LLM.chat(
            llm_messages
        )

        profiler.checkpoint(
            "LLM"
        )

        # ---------- Simpan Assistant ----------

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

        profiler.checkpoint(
            "Save Conversation"
        )

        profiler.finish()

        # ---------- Sources ----------

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