from app.services.fund.domain.repository.fund import FundRepositoryInterface
from app.services.fund.domain.query.query_interface import QueryInterface


class FundManagerHandler():

    def __init__(self, repository: FundRepositoryInterface, query: QueryInterface, skip: int = 0, take: int = 10, start_year: int = None, manager: str = None, name: str = None) -> None:
        self.id = id
        self.repository = repository
        self.query = query
        self.skip = skip
        self.take = take
        self.start_year = start_year
        self.manager = manager
        self.name = name

    def handler(self):
        r = self.query.handler(repository=self.repository,
                               skip=self.skip, take=self.take, start_year=self.start_year, manager=self.manager, name=self.name)
        return r
