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

        print("=" * 60)
        print("CHAT SERVICE")

        print("1. Retriever...")
        chunks = Retriever.search(
            workspace_id=workspace_id,
            query=question,
        )
        print("   ✓ Retriever selesai")

        print("2. Context Builder...")
        context = ContextBuilder.build(chunks)
        print("   ✓ Context selesai")

        print("3. Prompt Builder...")
        prompt = PromptBuilder.build(
            question=question,
            context=context,
        )

        print("=" * 50)
        print("Prompt Length :", len(prompt))
        print("=" * 50)
        print(prompt[:1000])
        print("=" * 50)
        print("   ✓ Prompt selesai")

        print("4. LLM...")
        answer = LLM.chat(prompt)
        print("   ✓ LLM selesai")

        print("5. Menyusun Citation...")

        sources = []

        for chunk in chunks:

            sources.append({
                "title": chunk.metadata.get("title"),
                "type": chunk.metadata.get("type"),
                "pages": chunk.metadata.get("pages"),
                "chunk_index": chunk.metadata.get("chunk_index"),
                "score": chunk.score,
            })

        print("   ✓ Citation selesai")

        print("6. Return")

        return {
            "answer": answer,
            "chunks": len(chunks),
            "sources": sources,
        }