from app.services.company.domain.repository.company import CompanyRepositoryInterface
from app.services.company.domain.query.query_interface import QueryInterface


class QueryCompaniesHandler():

    def __init__(self, repository: CompanyRepositoryInterface, query: QueryInterface) -> None:
        self.repository = repository
        self.query = query

    def handler(self):
        r = self.query.handler(repository=self.repository)
        return r
