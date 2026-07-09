from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from uuid import uuid4

from app.database.base import Base


class WorkspaceDB(Base):
    __tablename__ = "workspaces"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))

    name = Column(String, nullable=False)

    documents = relationship(
        "DocumentDB", back_populates="workspace", cascade="all, delete-orphan"
    )
