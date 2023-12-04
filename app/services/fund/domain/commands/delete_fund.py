from app.services.fund.domain.repository.fund import FundRepositoryInterface
from app.services.fund.domain.commands.command_interface import CommandInterface
from app.shared.domain.models.fund import Fund


class DeleteFund(CommandInterface):

    def handler(self, repository: FundRepositoryInterface, fund: Fund):
        try:
            repository.delete(fund=fund)
        except Exception:
            raise
