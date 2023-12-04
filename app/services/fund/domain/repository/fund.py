from abc import ABC
from app.shared.domain.models.fund import Fund
from app.shared.domain.models.log import Log
from app.shared.domain.models.manager import Manager


class FundRepositoryInterface(ABC):

    def add(self, fund: Fund) -> None:
        raise NotImplemented()

    def find(self, fund_id: str):
        raise NotImplemented()

    def find_companies(self, companies: list):
        raise NotImplemented()

    def find_manager(self, manager: str):
        raise NotImplemented()

    def find_duplicate(self, fund: Fund):
        raise NotImplemented()

    def list(skip: int, take: int):
        raise NotImplemented()

    def add_duplicate_fund(self, log: Log):
        raise NotImplemented()

    def delete(self, fund_id: str):
        raise NotImplemented()

    def update(self, fund_id: str, fund: object, manager: Manager, companies: list):
        raise NotImplemented()
