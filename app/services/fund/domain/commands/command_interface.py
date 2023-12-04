from abc import ABC
from app.services.fund.domain.repository.fund import FundRepositoryInterface
from app.shared.domain.models.fund import Fund
from app.shared.domain.models.log import Log


class CommandInterface(ABC):

    def handler(self, repository: FundRepositoryInterface, fund: Fund):
        raise NotImplemented()
