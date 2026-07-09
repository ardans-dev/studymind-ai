from app.memory.conversation_store import ConversationStore
from app.models.message import Message

ConversationStore.add_message(
    "AI",
    Message(
        role="user",
        content="Halo",
    ),
)

ConversationStore.add_message(
    "AI",
    Message(
        role="assistant",
        content="Halo juga!",
    ),
)

messages = ConversationStore.get_messages("AI")

for message in messages:
    print(message.role)
    print(message.content)
    print("-" * 30)