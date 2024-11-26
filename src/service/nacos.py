from nacos import NacosClient
from src.core.config import settings

class NacosService:
    def __init__(self):
        self.client = NacosClient(
            server_addresses=settings.NACOS_SERVER,
            namespace=settings.NACOS_NAMESPACE
        )
        
    async def register(self):
        self.client.add_naming_instance(
            settings.SERVICE_NAME,
            settings.SERVICE_IP,
            settings.SERVICE_PORT
        )
        
    async def heartbeat(self):
        await self.register()
        
    async def register_services(self):
        # 注册主服务
        await self.register_main_service()
        # 注册数据收集服务
        await self.register_data_service()
        # 注册预测服务
        await self.register_prediction_service()
