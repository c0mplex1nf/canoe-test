from app.services.company.domain.repository.company import CompanyRepositoryInterface
from app.services.company.domain.commands.command_interface import CommandInterface


class QueryCompany(CommandInterface):

    def handler(self, repository: CompanyRepositoryInterface, company_name: str):
        try:
            r = repository.get_company(company_name)
            return r
        except Exception:
            raise
