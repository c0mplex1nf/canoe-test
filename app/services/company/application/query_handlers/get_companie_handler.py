from app.services.company.domain.repository.company import CompanyRepositoryInterface
from app.services.company.domain.query.query_interface import QueryInterface


class QueryCompanyHandler():

    def __init__(self, repository: CompanyRepositoryInterface, query: QueryInterface, company_name: str) -> None:
        self.company_name = company_name
        self.repository = repository
        self.query = query

    def handler(self):
        r = self.query.handler(repository=self.repository,
                               company_name=self.company_name)
        return r
