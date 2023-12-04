from app.services.manager.domain.repository.manager import ManagerRepositoryInterface
from app.services.manager.domain.query.query_interface import QueryInterface


class QueryManagers(QueryInterface):

    def handler(self, repository: ManagerRepositoryInterface):
        try:
            r = repository.list()
            return r
        except Exception:
            raise
