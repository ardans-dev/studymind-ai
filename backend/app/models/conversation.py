from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Conversation:

    id: str

    workspace_id: str

    created_at: datetime = field(
        default_factory=datetime.now
    )