from sqlalchemy.orm import Session

from app.repositories.workspace_repository import WorkspaceRepository


class WorkspaceService:

    @staticmethod
    def create(db: Session, name: str):

        return WorkspaceRepository.create(db, name)

    @staticmethod
    def list(db: Session):

        return WorkspaceRepository.list(db)