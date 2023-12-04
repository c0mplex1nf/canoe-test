import requests
import uuid
import os
from datetime import datetime
from app.shared.domain.models.company import Company
from app.shared.domain.models.log import Log
from app.services.company.domain.events.company_created import CompanyCreated
from app.shared.domain.queue_interface import QueueClientInterface
from app.services.company.domain.commands.command_interface import CommandInterface
from app.services.company.domain.events.company_event_bus_interface import CompanyEventBusInterface
from app.services.company.domain.repository.company import CompanyRepositoryInterface


class CreateCompanyHandler():

    def __init__(self, company: object, command: CommandInterface, repository: CompanyRepositoryInterface, event_bus: CompanyEventBusInterface) -> None:
        self.bus = event_bus
        self.repository = repository
        self.command = command
        self.company = company

    def handler(self):
        id = str(uuid.uuid4())
        company = Company(
            id=id, name=self.company.name)

        self.command.handler(
            company=company, repository=self.repository)
