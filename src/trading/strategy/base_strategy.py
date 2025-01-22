from abc import ABC, abstractmethod
from typing import Dict
from core.event_bus import EventBus

class BaseStrategy(ABC):
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.position = 0
        self.active = False
        
    @abstractmethod
    async def analyze(self, market_data: Dict) -> Dict:
        """Analyze market data and return trading signals"""
        pass
        
    async def execute(self, signal: Dict):
        """Execute trading signals with risk management"""
        if self.active and self._validate_risk(signal):
            await self.event_bus.publish("order.new", signal)
            
    def _validate_risk(self, signal: Dict) -> bool:
        # Implement risk validation logic
        return True 