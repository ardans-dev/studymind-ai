from app.models.conversation import Conversation
from app.models.message import Message

conversation = Conversation(
    id="conv-001",
    workspace_id="AI",
)

message = Message(
    role="user",
    content="Apa itu analisis korelasi?",
)

print(conversation)
print(message)