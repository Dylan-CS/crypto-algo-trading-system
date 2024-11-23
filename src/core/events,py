from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from src.services.nacos import NacosService

async def start_scheduler(app: FastAPI) -> None:
    scheduler = AsyncIOScheduler(timezone="Asia/Shanghai")
    nacos_service = NacosService()
    
    scheduler.add_job(
        nacos_service.heartbeat, 
        'interval', 
        seconds=5
    )
    scheduler.start()
    app.state.scheduler = scheduler

async def stop_scheduler(app: FastAPI) -> None:
    app.state.scheduler.shutdown()
