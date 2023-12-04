from app.services.manager.domain.repository.manager import ManagerRepositoryInterface
from app.services.manager.domain.query.query_interface import QueryInterface


class QueryManagersHandler():

    def __init__(self, repository: ManagerRepositoryInterface, query: QueryInterface) -> None:
        self.repository = repository
        self.query = query

    def handler(self):
        r = self.query.handler(repository=self.repository)
        return r
