from typing import List
from dataclasses import dataclass, field
from app.shared.domain.models.company import Company
from app.shared.domain.models.manager import Manager


@dataclass(unsafe_hash=True)
class Fund:
    id: str
    name: str
    start_year: str
    alias: str
    nationality: str
    manager: Manager
    companies: List[Company] = field(default_factory=list)

    def serialize(obj):
        if isinstance(obj, (Company, Fund)):
            if isinstance(obj, Company):
                return {'id': obj.id, 'name': obj.name}
            elif isinstance(obj, Fund):
                return {'id': obj.id, 'name': obj.name, 'start_year': obj.start_year, 'alias': obj.alias, 'nationality': obj.nationality,
                        'manager': {'id': obj.manager.id, 'name': obj.manager.name}, 'companies': [Fund.serialize(c) for c in obj.companies]}
            elif isinstance(obj, Manager):
                return {'id': obj.id, 'name': obj.name}
        return None
