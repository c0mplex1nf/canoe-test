from app.services.company.domain.repository.company import CompanyRepositoryInterface
from app.services.company.domain.commands.command_interface import CommandInterface


class QueryCompanies(CommandInterface):

    def handler(self, repository: CompanyRepositoryInterface):
        try:
            r = repository.list()
            return r
        except Exception:
            raise
