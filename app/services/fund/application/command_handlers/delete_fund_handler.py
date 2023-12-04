from app.shared.domain.models.fund import Fund
from app.services.fund.domain.events.duplicate_fund_tried import FundDuplicated
from app.shared.domain.queue_interface import QueueClientInterface
from app.services.fund.domain.commands.command_interface import CommandInterface
from app.services.fund.domain.events.fund_event_bus_interface import FundEventBusInterface
from app.services.fund.domain.repository.fund import FundRepositoryInterface


class DeleteFundHandler():

    def __init__(self, fund_id: str, command: CommandInterface, repository: FundRepositoryInterface) -> None:
        self.repository = repository
        self.command = command
        self.fund_id = fund_id

    def handler(self):
        fund = self.repository.find(self.fund_id)

        if not fund:
            return 'The Fund does not exist'

        self.command.handler(
            fund=fund, repository=self.repository)
