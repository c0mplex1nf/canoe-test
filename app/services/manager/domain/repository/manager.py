from abc import ABC
from app.shared.domain.models.manager import Manager
from app.shared.domain.models.log import Log


class ManagerRepositoryInterface(ABC):

    def add(self, manager: Manager) -> None:
        raise NotImplemented()

    def list(self):
        raise NotImplemented()
