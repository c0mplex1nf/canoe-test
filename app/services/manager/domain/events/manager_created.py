from dataclasses import dataclass
from app.services.manager.domain.events.event_interface import EventInterface


@dataclass(unsafe_hash=True)
class ManagerCreated(EventInterface):
    name: str = 'manager-created'
