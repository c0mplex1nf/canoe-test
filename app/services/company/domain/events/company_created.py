from dataclasses import dataclass, field
from typing import List, Callable
from app.shared.domain.models.company import Company
from app.services.company.domain.events.event_interface import EventInterface


@dataclass(unsafe_hash=True)
class CompanyCreated(EventInterface):
    name: str = 'company-created'
