from app.services.company.domain.repository.company import CompanyRepositoryInterface
from app.services.company.domain.commands.command_interface import CommandInterface
from app.shared.domain.models.company import Company
from app.shared.domain.models.log import Log


class CreateCompany(CommandInterface):

    def handler(self, repository: CompanyRepositoryInterface, company: Company):
        try:
            repository.add(company)
        except Exception:
            raise
