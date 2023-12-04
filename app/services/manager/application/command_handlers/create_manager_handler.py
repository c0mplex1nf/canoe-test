import uuid
from app.shared.domain.models.manager import Manager
from app.services.manager.domain.commands.command_interface import CommandInterface
from app.services.manager.domain.events.manager_event_bus_interface import ManagerEventBusInterface
from app.services.manager.domain.repository.manager import ManagerRepositoryInterface


class CreateManagerHandler():

    def __init__(self, manager: object, command: CommandInterface, repository: ManagerRepositoryInterface, event_bus: ManagerEventBusInterface) -> None:
        self.bus = event_bus
        self.repository = repository
        self.command = command
        self.manager = manager

    def handler(self):
        id = str(uuid.uuid4())
        manager = Manager(
            id=id, name=self.manager.name)

        self.command.handler(
            manager=manager, repository=self.repository)

        # event = ManagerCreated(func_name=self.team_queue.send_message, data={
        # 'league_id': id, 'code': self.code})
        # self.bus.add_listener(event)
        # self.bus.emit(event)
        # self.bus.remove_listener(event)
