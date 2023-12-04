import requests
import uuid
import os
import json
from datetime import datetime
from app.shared.domain.models.fund import Fund
from app.shared.domain.models.log import Log
from app.services.fund.domain.events.duplicate_fund_tried import FundDuplicated
from app.shared.domain.queue_interface import QueueClientInterface
from app.services.fund.domain.commands.command_interface import CommandInterface
from app.services.fund.domain.events.fund_event_bus_interface import FundEventBusInterface
from app.services.fund.domain.repository.fund import FundRepositoryInterface


class CreateFundHandler():

    def __init__(self, fund: object, command: CommandInterface, repository: FundRepositoryInterface, event_bus: FundEventBusInterface, duplicated_queue: QueueClientInterface) -> None:
        self.bus = event_bus
        self.repository = repository
        self.command = command
        self.fund = fund
        self.duplicated_queue = duplicated_queue

    def handler(self):
        id = str(uuid.uuid4())
        manager = self.repository.find_manager(self.fund.manager)

        if not manager:
            return 'There was not manager with this id'

        companies = self.repository.find_companies(self.fund.companies)

        fund = Fund(
            id=id, name=self.fund.name, start_year=self.fund.start_year, alias=self.fund.alias, nationality=self.fund.nationality, manager=manager, companies=companies
        )

        duplicate_fund = self.repository.find_duplicate(fund)

        if len(duplicate_fund) > 0:
            data = Fund.serialize(fund)
            event = FundDuplicated(
                func_name=self.duplicated_queue.send_message, data=data)
            self.bus.add_listener(event)
            self.bus.emit(event)
            self.bus.remove_listener(event)
            return 'There was a duplicate Fund'

        self.command.handler(
            fund=fund, repository=self.repository)
