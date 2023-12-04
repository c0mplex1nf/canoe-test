from app.services.fund.domain.repository.fund import FundRepositoryInterface
from app.services.fund.domain.commands.command_interface import CommandInterface
from app.shared.domain.models.fund import Fund
from app.shared.domain.models.manager import Manager


class UpdateFund(CommandInterface):

    def handler(self, repository: FundRepositoryInterface, fund_id: str, fund: object, manager: Manager, companies: list):
        try:
            repository.update(fund_id=fund_id, fund=fund,
                              manager=manager, companies=companies)
        except Exception:
            raise
