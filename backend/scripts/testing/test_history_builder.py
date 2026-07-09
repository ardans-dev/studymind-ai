from app.models.message import Message
from app.rag.history_builder import HistoryBuilder

messages = [
    Message(
        role="user",
        content="Apa itu AI?",
    ),
    Message(
        role="assistant",
        content="AI adalah kecerdasan buatan.",
    ),
    Message(
        role="user",
        content="Berikan contohnya.",
    ),
]

print(
    HistoryBuilder.build(messages)
)