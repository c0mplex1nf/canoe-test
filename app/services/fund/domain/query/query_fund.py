from app.services.fund.domain.repository.fund import FundRepositoryInterface
from app.services.fund.domain.commands.command_interface import CommandInterface


class QueryFunds(CommandInterface):

    def handler(self, repository: FundRepositoryInterface, skip: int = 0, take: int = 10, start_year: int = None, manager: str = None, name: str = None):
        try:
            r = repository.list(
                skip=skip, take=take, start_year=start_year, manager=manager, name=name)
            return r
        except Exception:
            raise
