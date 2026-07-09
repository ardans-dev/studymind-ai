from uuid import uuid4

from sqlalchemy import Column, ForeignKey, String, Text

from app.database.base import Base


class ConversationDB(Base):
    __tablename__ = "conversations"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    workspace_id = Column(
        String,
        ForeignKey("workspaces.id"),
        nullable=False,
    )

    role = Column(
        String,
        nullable=False,
    )

    content = Column(
        Text,
        nullable=False,
    )