from abc import ABC, abstractmethod
from typing import Dict, Any
from core.event_bus import EventBus

class BaseDataCollector(ABC):
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        
    @abstractmethod
    async def start(self):
        pass
        
    @abstractmethod
    async def stop(self):
        pass
        
    async def publish_data(self, data_type: str, data: Dict[str, Any]):
        await self.event_bus.publish(f"market_data.{data_type}", data) 