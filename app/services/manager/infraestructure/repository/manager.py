from fastapi import Depends
from sqlalchemy import insert
from app.services.manager.domain.repository.manager import ManagerRepositoryInterface
from app.shared.domain.models.manager import Manager
from config.database import get_session


class ManagerSqlAlchemyRepository(ManagerRepositoryInterface):

    def __init__(self, session=Depends(get_session)):
        self.session = session

    def add(self, manager: Manager):
        self.session.add(manager)
        self.session.commit()

    def list(self):
        r = self.session.query(Manager).all()
        return r
