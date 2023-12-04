import json
from fastapi import APIRouter, Depends, Request
from pydantic import ValidationError
from app.services.fund.presentation.controllers.controller import Controller
from app.services.fund.application.command_handlers.create_fund_handler import CreateFundHandler
from app.services.fund.application.command_handlers.delete_fund_handler import DeleteFundHandler
from app.services.fund.application.command_handlers.update_fund_handler import UpdateFundHandler
from app.services.fund.domain.commands.create_fund import CreateFund
from app.services.fund.domain.commands.update_fund import UpdateFund
from app.services.fund.domain.commands.delete_fund import DeleteFund
from app.services.fund.infraestructure.repository.fund import FundSqlAlchemyRepository
from app.shared.infraestructure.event_bus import EventBus
from app.shared.infraestructure.fund_duplicated_queue_client import FundDuplicateQueueClient
from app.services.fund.presentation.dto.fund import FundDTO
from app.services.fund.application.query_handlers.get_funds_handler import FundManagerHandler
from app.services.fund.application.query_handlers.get_duplicate_funds_handler import DuplicateFundManagerHandler
from app.services.fund.domain.query.query_fund import QueryFunds
from app.services.fund.domain.query.query_duplicate_fund import QueryDuplicateFunds


class FundController(Controller):

    router = APIRouter()

    def __init__(self) -> None:
        super().__init__()

    @router.post('/')
    async def create(request: Request, command=Depends(CreateFund), repository=Depends(FundSqlAlchemyRepository),
                     event_bus=Depends(EventBus), fund_duplicated_queue=Depends(FundDuplicateQueueClient)) -> json:

        try:
            fund_info = await request.json()
            fund = FundDTO(
                name=fund_info['name'],
                start_year=fund_info['start_year'],
                alias=fund_info['alias'],
                nationality=fund_info['nationality'],
                manager=fund_info['manager'],
                companies=fund_info['companies']
            )
        except ValidationError as e:
            return e.errors()

        response = {'message': 'The Fund have been saved'}
        handler = CreateFundHandler(
            fund=fund, command=command, repository=repository, event_bus=event_bus, duplicated_queue=fund_duplicated_queue)
        errors = handler.handler()

        if errors:
            response['message'] = errors

        return response

    @router.put('/{fund_id}')
    async def update(request: Request, fund_id: str, command=Depends(UpdateFund), repository=Depends(FundSqlAlchemyRepository),
                     event_bus=Depends(EventBus), fund_duplicated_queue=Depends(FundDuplicateQueueClient)) -> json:

        try:
            fund_info = await request.json()
            fund = FundDTO(
                name=fund_info['name'],
                start_year=fund_info['start_year'],
                alias=fund_info['alias'],
                nationality=fund_info['nationality'],
                manager=fund_info['manager'],
                companies=fund_info['companies']
            )
        except ValidationError as e:
            return e.errors()

        response = {'message': 'The Fund have been updated'}
        handler = UpdateFundHandler(
            fund_id=fund_id, fund=fund, command=command, repository=repository, event_bus=event_bus, duplicated_queue=fund_duplicated_queue)
        errors = handler.handler()

        if errors:
            response['message'] = errors

        return response

    @router.delete('/{fund_id}')
    async def update(fund_id: str, command=Depends(DeleteFund), repository=Depends(FundSqlAlchemyRepository),
                     event_bus=Depends(EventBus)) -> json:

        response = {'message': 'The Fund have been deleted'}
        handler = DeleteFundHandler(
            fund_id=fund_id, command=command, repository=repository)
        errors = handler.handler()

        if errors:
            response['message'] = errors

        return response

    @router.get('/')
    async def list(skip: int = 0, take: int = 10, start_year: int = None, manager: str = None, name: str = None, repository=Depends(FundSqlAlchemyRepository), query=Depends(QueryFunds)) -> json:
        response = {}

        query_handler = FundManagerHandler(
            repository=repository, query=query, skip=skip, take=take,  start_year=start_year, manager=manager, name=name)

        query_response = query_handler.handler()
        response['body'] = query_response
        return response

    @router.get('/duplicate')
    async def list_duplicates(skip: int = 0, take: int = 10, repository=Depends(FundSqlAlchemyRepository), query=Depends(QueryDuplicateFunds)) -> json:
        response = {}

        query_handler = DuplicateFundManagerHandler(
            repository=repository, query=query, skip=skip, take=take)

        query_response = query_handler.handler()
        response['body'] = query_response
        return response
