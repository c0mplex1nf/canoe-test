from dataclasses import dataclass, field
from typing import List


@dataclass(unsafe_hash=True)
class Manager:
    id: str
    name: str
