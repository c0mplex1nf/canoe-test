from abc import ABC
from app.shared.domain.models.company import Company
from app.shared.domain.models.log import Log


class CompanyRepositoryInterface(ABC):

    def add(self, company: Company) -> None:
        raise NotImplemented()

    def get_company(self, company_name):
        raise NotImplemented()

    def list(self):
        raise NotImplemented()
