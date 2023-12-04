from app.services.manager.domain.repository.manager import ManagerRepositoryInterface
from app.services.manager.domain.commands.command_interface import CommandInterface
from app.shared.domain.models.manager import Manager
from app.shared.domain.models.log import Log


class CreateManager(CommandInterface):

    def handler(self, repository: ManagerRepositoryInterface, manager: Manager):
        try:
            repository.add(manager)
        except Exception:
            raise
