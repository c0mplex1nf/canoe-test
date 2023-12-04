import json
from app.services.fund.domain.repository.fund import FundRepositoryInterface
from app.services.fund.domain.query.query_interface import QueryInterface


class DuplicateFundManagerHandler():

    def __init__(self, repository: FundRepositoryInterface, query: QueryInterface, skip: int = 0, take: int = 10) -> None:
        self.id = id
        self.repository = repository
        self.query = query
        self.skip = skip
        self.take = take

    def handler(self):
        r = self.query.handler(repository=self.repository,
                               skip=self.skip, take=self.take)
        logs = []
        for log in r:
            log.created_at = log.created_at.strftime('%Y-%m-%d %H:%M:%S')
            log.data = json.loads(log.data)
            logs.append(log)

        return logs
