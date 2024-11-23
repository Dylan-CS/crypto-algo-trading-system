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
