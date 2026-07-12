import logging
from pathlib import Path

# Membuat folder logs jika belum ada
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

logger = logging.getLogger("StudyMind")

if not logger.handlers:

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )

    # Simpan ke file
    file_handler = logging.FileHandler(
        log_dir / "studymind.log",
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    # Tampilkan di terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.propagate = False