from dataclasses import dataclass, field
from typing import List


@dataclass
class Workspace:
    id: str
    name: str
    documents: List[str] = field(default_factory=list)
