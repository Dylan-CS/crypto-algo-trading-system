import aio_pika
import asyncio
from src.core.config import settings

class EventConsumer:
    def __init__(self):
        self.connection = None
        self.channel = None

    async def connect(self):
        self.connection = await aio_pika.connect_robust(settings.RABBITMQ_URL)
        self.channel = await self.connection.channel()

    async def consume(self, queue_name: str, callback):
        queue = await self.channel.declare_queue(queue_name)
        await queue.consume(callback)

    async def close(self):
        await self.connection.close() 