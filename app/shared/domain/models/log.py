from dataclasses import dataclass, field
from typing import List
from datetime import datetime


@dataclass(unsafe_hash=True)
class Log:
    id: str
    data: str
    created_at: datetime = field(default_factory=datetime.now)
