import uuid
import json
from app.shared.domain.models.fund import Fund
from app.shared.domain.models.manager import Manager
from app.shared.domain.models.log import Log
from app.services.fund.domain.repository.fund import FundRepositoryInterface
from app.services.fund.domain.commands.command_interface import CommandInterface


class CreateDuplicateFundRegisterHandler():

    def __init__(self, fund: Fund, command: CommandInterface, repository: FundRepositoryInterface,) -> None:
        self.fund = fund
        self.repository = repository
        self.command = command

    def handler(self):
        id = str(uuid.uuid4())
        json_data = json.dumps(self.fund, default=Fund.serialize)
        log = Log(id=id, data=json_data)

        self.command.handler(
            log=log, repository=self.repository)
