from typing import Dict, Callable, Any
from asyncio import Queue
import asyncio

class EventBus:
    def __init__(self):
        self._subscribers: Dict[str, list[Queue]] = {}
        
    async def publish(self, event_type: str, data: Any):
        if event_type in self._subscribers:
            for queue in self._subscribers[event_type]:
                await queue.put(data)
                
    async def subscribe(self, event_type: str) -> Queue:
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        queue = Queue()
        self._subscribers[event_type].append(queue)
        return queue 