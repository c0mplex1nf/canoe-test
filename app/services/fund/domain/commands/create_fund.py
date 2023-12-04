from app.services.fund.domain.repository.fund import FundRepositoryInterface
from app.services.fund.domain.commands.command_interface import CommandInterface
from app.shared.domain.models.fund import Fund
from app.shared.domain.models.log import Log


class CreateFund(CommandInterface):

    def handler(self, repository: FundRepositoryInterface, fund: Fund):
        try:
            repository.add(fund)
        except Exception:
            raise
