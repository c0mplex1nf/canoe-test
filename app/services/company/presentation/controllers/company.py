import json
from fastapi import APIRouter, Depends, Request
from pydantic import ValidationError
from app.services.company.presentation.controllers.controller import Controller
from app.services.company.application.command_handlers.create_company_handler import CreateCompanyHandler
from app.services.company.application.query_handlers.get_companies_handler import QueryCompaniesHandler
from app.services.company.domain.commands.create_company import CreateCompany
from app.services.company.infraestructure.repository.company import CompanySqlAlchemyRepository
from app.shared.infraestructure.event_bus import EventBus
from app.services.company.domain.query.query_companies import QueryCompanies
from app.services.company.presentation.dto.company import CompanyDTO


class CompanyController(Controller):

    router = APIRouter()

    def __init__(self) -> None:
        super().__init__()

    @router.post('/')
    async def create(request: Request, command=Depends(CreateCompany), repository=Depends(CompanySqlAlchemyRepository),
                     event_bus=Depends(EventBus)) -> json:

        try:
            company_info = await request.json()
            company = CompanyDTO(name=company_info['name'])
        except ValidationError as e:
            return e.errors()

        response = {'message': 'The Company have been saved'}
        handler = CreateCompanyHandler(
            company=company, command=command, repository=repository, event_bus=event_bus)
        errors = handler.handler()

        if errors:
            response['message'] = errors

        return response

    @router.get('/')
    async def list(repository=Depends(CompanySqlAlchemyRepository), query=Depends(QueryCompanies)):
        response = {}
        query_handler = QueryCompaniesHandler(
            repository=repository, query=query)
        query_response = query_handler.handler()
        response['body'] = query_response
        return response
