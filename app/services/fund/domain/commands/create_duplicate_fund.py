from app.services.fund.domain.repository.fund import FundRepositoryInterface
from app.services.fund.domain.commands.command_interface import CommandInterface
from app.shared.domain.models.log import Log


class CreateDuplicateFund(CommandInterface):

    def handler(self, repository: FundRepositoryInterface, log: Log):
        try:
            repository.add_duplicate_fund(log=log)
        except Exception:
            raise
