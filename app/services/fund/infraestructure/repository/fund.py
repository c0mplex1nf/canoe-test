from fastapi import Depends
from sqlalchemy import func
from app.services.fund.domain.repository.fund import FundRepositoryInterface
from app.shared.domain.models.fund import Fund
from app.shared.domain.models.log import Log
from app.shared.domain.models.company import Company
from app.shared.domain.models.manager import Manager
from config.database import get_session


class FundSqlAlchemyRepository(FundRepositoryInterface):

    def __init__(self, session=Depends(get_session)):
        self.session = session

    def add(self, fund: Fund):
        with self.session as session:
            session.add(fund)
            session.commit()

    def find_companies(self, companies: list):
        r = self.session.query(Company).filter(
            Company.id.in_(companies)).all()

        return r

    def find_manager(self, manager_id: str):
        r = self.session.query(Manager).get(manager_id)

        return r

    def list_duplicates(self, skip: int = 0, take: int = 10):
        r = self.session.query(Log).limit(take).offset(skip).all()
        return r

    def find_duplicate(self, fund: Fund):
        r = self.session.query(Fund).filter(
            ((Fund.alias == fund.alias) | (Fund.name == fund.name)),
            (Fund.manager.has(id=fund.manager.id))
        ).all()
        return r

    def find(self, fund_id: str):
        r = self.session.query(Fund).get(fund_id)
        return r

    def list(self, skip: int = 0, take: int = 10, start_year: int = None, manager: str = None, name: str = None):

        r = self.session.query(Fund)

        if name:
            r = r.filter(Fund.name == name)
        if manager:
            r = r.filter(Fund.manager.has(id=manager))
        if start_year:
            r = r.filter(Fund.start_year == start_year)

        r = r.limit(take).offset(skip).all()

        return r

    def add_duplicate_fund(self, log: Log):
        with self.session as session:
            with session.no_autoflush:
                session.add(log)
                session.commit()

    def delete(self, fund: Fund):
        with self.session as session:
            fund.companies.clear()
            session.query(Fund).filter(Fund.id == fund.id).delete()
            session.commit()

    def update(self, fund_id: str, fund: object, manager: Manager, companies: list):
        with self.session as session:
            with session.no_autoflush:
                r = self.session.query(Fund).get(fund_id)
                r.id = fund_id
                r.name = fund.name
                r.start_year = fund.start_year
                r.alias = fund.alias
                r.nationality = fund.nationality
                r.manager = manager
                r.companies = companies
                session.commit()
