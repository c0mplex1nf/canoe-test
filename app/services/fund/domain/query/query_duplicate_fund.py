from app.services.fund.domain.repository.fund import FundRepositoryInterface
from app.services.fund.domain.commands.command_interface import CommandInterface


class QueryDuplicateFunds(CommandInterface):

    def handler(self, repository: FundRepositoryInterface, skip: int = 0, take: int = 10):
        try:
            r = repository.list_duplicates(skip=skip, take=take)
            return r
        except Exception:
            raise
