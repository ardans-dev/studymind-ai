from abc import ABC, abstractmethod
from app.models.document import Document


class BaseParser(ABC):

    @abstractmethod
    def parse(self, filepath: str) -> Document:
        pass