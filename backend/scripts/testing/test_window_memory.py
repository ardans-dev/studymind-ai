from app.memory.conversation_store import ConversationStore
from app.models.message import Message

ConversationStore.clear("AI")

for i in range(15):
    ConversationStore.add_message(
        "AI",
        Message(
            role="user",
            content=f"Message {i + 1}",
        ),
    )

messages = ConversationStore.get_messages("AI")

print("Jumlah Message:", len(messages))

for message in messages:
    print(message.content)