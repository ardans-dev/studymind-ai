from app.database.database import engine
from app.database.base import Base

# Penting: import semua model agar terdaftar

Base.metadata.create_all(bind=engine)

print("Database berhasil dibuat!")
