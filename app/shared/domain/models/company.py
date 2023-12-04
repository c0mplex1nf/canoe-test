from dataclasses import dataclass, field


@dataclass(unsafe_hash=True)
class Company:
    id: str
    name: str
