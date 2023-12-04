import json
from fastapi import APIRouter, Depends, Request
from pydantic import ValidationError
from app.services.manager.presentation.controllers.controller import Controller
from app.services.manager.application.command_handlers.create_manager_handler import CreateManagerHandler
from app.services.manager.application.query_handlers.get_managers_handler import QueryManagersHandler
from app.services.manager.domain.commands.create_manager import CreateManager
from app.services.manager.infraestructure.repository.manager import ManagerSqlAlchemyRepository
from app.shared.infraestructure.event_bus import EventBus
from app.services.manager.presentation.dto.manager import ManagerDTO
from app.services.manager.domain.query.query_managers import QueryManagers


class ManagerController(Controller):

    router = APIRouter()

    def __init__(self) -> None:
        super().__init__()

    @router.post('/')
    async def create(request: Request, command=Depends(CreateManager), repository=Depends(ManagerSqlAlchemyRepository),
                     event_bus=Depends(EventBus)) -> json:

        try:
            manager_info = await request.json()
            manager = ManagerDTO(
                name=manager_info['name'])
        except ValidationError as e:
            return e.errors()

        response = {'message': 'The Manager have been saved'}
        handler = CreateManagerHandler(
            manager=manager, command=command, repository=repository, event_bus=event_bus)
        errors = handler.handler()

        if errors:
            response['message'] = errors

        return response

    @router.get('/')
    async def list(repository=Depends(ManagerSqlAlchemyRepository), query=Depends(QueryManagers)):
        response = {}
        query_handler = QueryManagersHandler(
            repository=repository, query=query)
        query_response = query_handler.handler()
        response['body'] = query_response
        return response
