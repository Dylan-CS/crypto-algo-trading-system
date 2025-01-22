from fastapi import FastAPI
from core.config import settings
from core.events import start_scheduler, stop_scheduler
from core.event_publisher import EventPublisher
from core.event_consumer import EventConsumer
from api.endpoints import health, predictions
import aio_pika
from service.newsbot import NewsBot
from data.pipeline import MarketDataPipeline
from strategy.news_sentiment_strategy import NewsSentimentStrategy

event_publisher = EventPublisher()
event_consumer = EventConsumer()

def create_application() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
    )
    
    app.include_router(
        health.router,
        prefix=settings.API_V1_STR
    )
    app.include_router(
        predictions.router,
        prefix=settings.API_V1_STR
    )

    @app.on_event("startup")
    async def startup_event():
        await event_publisher.connect()
        await event_consumer.connect()
        await event_consumer.consume("your_queue_name", your_callback_function)
        await start_scheduler(app)
        
        # 初始化新组件
        newsbot = NewsBot()
        pipeline = MarketDataPipeline()
        strategy = NewsSentimentStrategy(newsbot, pipeline)
        
        # 启动数据管道
        await pipeline.start()
        await pipeline.setup_handlers()
    
    @app.on_event("shutdown")
    async def shutdown_event():
        await stop_scheduler(app)
        await event_publisher.close()
        await event_consumer.close()
    
    return app

async def your_callback_function(message: aio_pika.IncomingMessage):
    async with message.process():
        print(f"Received message: {message.body.decode()}")
        # Handle the event here

app = create_application()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=settings.SERVICE_PORT,
        reload=True
    ) 