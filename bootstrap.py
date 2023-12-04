import asyncio
import os
from fastapi import FastAPI
from aio_pika import logger
from dotenv import load_dotenv
from config import database
from app.services.company.presentation.controllers.company import CompanyController
from app.services.manager.presentation.controllers.manager import ManagerController
from app.services.fund.presentation.controllers.fund import FundController
from app.shared.infraestructure.fund_duplicated_queue_client import FundDuplicateQueueClient


class Bootstrap(FastAPI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        self.company = CompanyController()
        self.manager = ManagerController()
        self.fund = FundController()
        self.metadata = database.start_mappers()
        self.fund_duplicated_queue_client = FundDuplicateQueueClient()


app = Bootstrap()
app.include_router(app.company.router, prefix="/company")
app.include_router(app.manager.router, prefix="/manager")
app.include_router(app.fund.router, prefix="/fund")


@app.on_event('startup')
async def startup():
    loop = asyncio.get_running_loop()
    task_duplicate_fund = loop.create_task(
        app.fund_duplicated_queue_client.consume(loop=loop))
    await task_duplicate_fund
