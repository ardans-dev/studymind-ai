import time

from app.core.logger import logger


class Profiler:
    """
    Mengukur waktu eksekusi setiap tahap proses.
    """

    def __init__(self):

        self.start = time.perf_counter()
        self.last = self.start

    def checkpoint(self, name: str):

        now = time.perf_counter()

        elapsed = now - self.last

        logger.info(
            f"{name:<25} : {elapsed:.3f} detik"
        )

        self.last = now

    def finish(self):

        total = time.perf_counter() - self.start

        logger.info("-" * 50)

        logger.info(
            f"{'TOTAL REQUEST':<25} : {total:.3f} detik"
        )

        logger.info("-" * 50)