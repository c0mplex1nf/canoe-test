from abc import ABC
from app.services.manager.domain.repository.manager import ManagerRepositoryInterface
from app.shared.domain.models.manager import Manager
from app.shared.domain.models.log import Log


class CommandInterface(ABC):

    def handler(self, repository: ManagerRepositoryInterface, manager: Manager):
        raise NotImplemented()
