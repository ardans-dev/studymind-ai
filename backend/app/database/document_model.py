from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class DocumentDB(Base):

    __tablename__ = "documents"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid4())
    )

    workspace_id = Column(
        String,
        ForeignKey("workspaces.id"),
        nullable=False
    )

    title = Column(String)

    path = Column(String)

    type = Column(String)

    pages = Column(Integer)

    workspace = relationship(
        "WorkspaceDB",
        back_populates="documents"
    )