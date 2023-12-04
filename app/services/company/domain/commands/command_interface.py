from abc import ABC
from app.services.company.domain.repository.company import CompanyRepositoryInterface
from app.shared.domain.models.company import Company
from app.shared.domain.models.log import Log


class CommandInterface(ABC):

    def handler(self, repository: CompanyRepositoryInterface, league: Company, log: Log):
        raise NotImplemented()
