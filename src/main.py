from fastapi import FastAPI
from core.config import settings
from core.events import start_scheduler, stop_scheduler
from api.endpoints import health, predictions
from services.nacos import NacosService

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
        nacos = NacosService()
        await nacos.register()
        await start_scheduler(app)
    
    @app.on_event("shutdown")
    async def shutdown_event():
        await stop_scheduler(app)
    
    return app

app = create_application()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=settings.SERVICE_PORT,
        reload=True
    ) 