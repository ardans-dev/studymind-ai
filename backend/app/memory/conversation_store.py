from app.models.message import Message
from app.repositories.conversation_repository import ConversationRepository
from app.core.config import settings

settings.MAX_HISTORY = 10

class ConversationStore:
    """
    Penyimpanan percakapan sementara (in-memory).
    Key = workspace_id
    Value = list[Message]
    """

    _store: dict[str, list[Message]] = {}

    @classmethod
    def add_message(
        cls,
        workspace_id: str,
        message: Message,
    ):

        if workspace_id not in cls._store:
            cls._store[workspace_id] = []

        cls._store[workspace_id].append(message)

        if len(cls._store[workspace_id]) > settings.settings.MAX_HISTORY:
            cls._store[workspace_id] = cls._store[workspace_id][-settings.MAX_HISTORY:]

    @classmethod
    def get_messages(
        cls,
        workspace_id: str,
    ) -> list[Message]:

        if workspace_id not in cls._store:

            conversations = ConversationRepository.load_messages(
                workspace_id
            )

            cls._store[workspace_id] = [
                Message(
                    role=item.role,
                    content=item.content,
                )
                for item in conversations
            ]

        return cls._store[workspace_id]

    @classmethod
    def clear(
        cls,
        workspace_id: str,
    ):

        cls._store.pop(
            workspace_id,
            None,
        )