from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.conversation_model import ConversationDB
from app.database.database import engine


class ConversationRepository:

    @staticmethod
    def save(conversation: ConversationDB):

        with Session(engine) as session:
            session.add(conversation)
            session.commit()

    @staticmethod
    def get_by_workspace(workspace_id: str):

        with Session(engine) as session:

            statement = (
                select(ConversationDB)
                .where(
                    ConversationDB.workspace_id == workspace_id
                )
            )

            return session.scalars(statement).all()
        
    @staticmethod
    def load_messages(workspace_id: str):

        conversations = ConversationRepository.get_by_workspace(
            workspace_id
        )

        return conversations