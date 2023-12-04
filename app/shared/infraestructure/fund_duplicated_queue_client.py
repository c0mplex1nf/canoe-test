import pika
import os
import json
import uuid
from aio_pika import connect_robust
from config.database import get_session
from app.shared.domain.models.fund import Fund
from app.shared.domain.models.manager import Manager
from app.shared.domain.models.company import Company
from app.services.fund.domain.commands.create_duplicate_fund import CreateDuplicateFund
from app.services.fund.infraestructure.repository.fund import FundSqlAlchemyRepository
from app.services.fund.application.command_handlers.create_fund_duplicate_register_handler import CreateDuplicateFundRegisterHandler


class FundDuplicateQueueClient:

    def __init__(self):
        self.queue_name = os.environ.get(
            'DUPLICATE_FUND_QUEUE', 'duplicate-fund-queue')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=os.environ.get(
                'RABBIT_HOST', 'rabbitmq'), heartbeat=0)
        )
        self.channel = self.connection.channel()
        self.queue = self.channel.queue_declare(queue=self.queue_name)
        self.callback_queue = self.queue.method.queue

    async def send_message(self, message: dict):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=str(uuid.uuid4())
            ),
            body=json.dumps(message)
        )

    async def process_incoming_message(self, message):
        await message.ack()
        body = message.body.decode("UTF-8")
        data = json.loads(body)

        if body:
            session = get_session()

            manager = Manager(**data['manager'])
            companies = []

            for company in data['companies']:
                companies.append(Company(**company))

            fund = Fund(id=data['id'], name=data['name'], start_year=data['start_year'], alias=data['alias'],
                        nationality=data['nationality'], manager=manager, companies=companies)

            fund_handler = CreateDuplicateFundRegisterHandler(
                fund=fund, repository=FundSqlAlchemyRepository(session=session), command=CreateDuplicateFund())
            fund_handler.handler()

    async def consume(self, loop):
        connection = await connect_robust(host=os.environ.get('RABBIT_HOST', 'rabbitmq'), port=5672, loop=loop)
        channel = await connection.channel()
        queue = await channel.declare_queue(self.queue_name)
        await queue.consume(self.process_incoming_message, no_ack=False)
        return connection
