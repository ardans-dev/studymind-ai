from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Chunk:
    id: int

    title: str

    content: str

    metadata: Dict = field(default_factory=dict)
