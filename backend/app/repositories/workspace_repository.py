from sqlalchemy.orm import Session

from app.database.models import WorkspaceDB


class WorkspaceRepository:

    @staticmethod
    def create(db: Session, name: str):

        workspace = WorkspaceDB(name=name)

        db.add(workspace)

        db.commit()

        db.refresh(workspace)

        return workspace

    @staticmethod
    def list(db: Session):

        return db.query(WorkspaceDB).all()