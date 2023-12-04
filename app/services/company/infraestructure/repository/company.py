from fastapi import Depends
from sqlalchemy import insert
from app.services.company.domain.repository.company import CompanyRepositoryInterface
from app.shared.domain.models.company import Company
from app.shared.domain.models.manager import Manager
from app.shared.domain.models.fund import Fund
from app.shared.domain.models.log import Log
from config.database import get_session


class CompanySqlAlchemyRepository(CompanyRepositoryInterface):

    def __init__(self, session=Depends(get_session)):
        self.session = session

    def add(self, company: Company):
        self.session.add(company)
        self.session.commit()

    def get_company(self, company_name=None):

        r = self.session.query(Fund).join(Company.managers).join(
            Manager.funds).filter(Company.name == company_name)

        return r.all()

    def list(self):
        r = self.session.query(Company).all()
        return r
