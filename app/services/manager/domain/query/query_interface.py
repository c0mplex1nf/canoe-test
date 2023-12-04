from abc import ABC
from app.services.company.domain.repository.company import CompanyRepositoryInterface


class QueryInterface(ABC):

    def handler(self, repository: CompanyRepositoryInterface, company_name: str):
        raise NotImplemented()
