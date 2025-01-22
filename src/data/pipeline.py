from typing import Callable, Awaitable, Dict, List
from aio_pika import IncomingMessage
from core.event_consumer import EventConsumer
from core.event_publisher import EventPublisher
from enum import Enum
from datetime import datetime

class EventType(Enum):
    NEWS_UPDATE = "news_update"
    SENTIMENT_UPDATE = "sentiment_update"
    PRICE_UPDATE = "price_update"
    TRADING_SIGNAL = "trading_signal"

class DataPipeline:
    def __init__(self):
        self.consumer = EventConsumer()
        self.publisher = EventPublisher()
        self.handlers = {}
        
    async def start(self):
        await self.consumer.connect()
        await self.publisher.connect()
        
    async def register_handler(self, event_type: str, handler: Callable[[dict], Awaitable[None]]):
        self.handlers[event_type] = handler
        await self.consumer.consume(event_type, self._create_callback(handler))
        
    def _create_callback(self, handler):
        async def callback(message: IncomingMessage):
            async with message.process():
                data = message.body.decode()
                await handler(data)
        return callback
    
    async def publish_event(self, event_type: str, data: dict):
        await self.publisher.publish(event_type, data)

class MarketDataPipeline(DataPipeline):
    async def setup_handlers(self):
        await self.register_handler(EventType.NEWS_UPDATE.value, self.handle_news)
        await self.register_handler(EventType.SENTIMENT_UPDATE.value, self.handle_sentiment)
        await self.register_handler(EventType.PRICE_UPDATE.value, self.handle_price)
        
    async def handle_news(self, data: dict):
        # Process news data
        sentiment = await self.newsbot.analyze_sentiment(data['content'])
        await self.publish_event(EventType.SENTIMENT_UPDATE.value, {
            'sentiment': sentiment,
            'timestamp': datetime.now().isoformat()
        })
