from dataclasses import dataclass
from app.services.fund.domain.events.event_interface import EventInterface


@dataclass(unsafe_hash=True)
class FundDuplicated(EventInterface):
    name: str = 'fund-duplicated'
