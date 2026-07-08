from app.database.database import engine
from app.database.base import Base

# Penting: import semua model agar terdaftar
from app.database.models import WorkspaceDB

Base.metadata.create_all(bind=engine)

print("Database berhasil dibuat!")