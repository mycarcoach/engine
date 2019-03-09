#!/usr/bin/env python
from enum import Enum
import json
import websockets
import asyncio

# provides the data acquired from the websocket server
class DataProvider:
    
    self.dataProviderSource
    self.data
    
    def __init__(self, dataProviderSource):
        self.dataProviderSource = dataProviderSource
        asyncio.get_event_loop().run_until_complete(handler())
    
    async def handler(self):
        async with websockets.connect(('ws://%s:8765', self.dataProviderSource) as websocket:
            jsons = await websocket.recv()
            self.data = json.loads(jsons)
    
    def getData(self):
        return self.data
            

class DataProviderSource(Enum):
    SIMULATION = "130.82.239.210"
    REAL = "192.168.8.10"
    