#!/usr/bin/env python
from enum import Enum
import json
import websockets
import asyncio

# provides the data acquired from the websocket server
class DataProvider:

    def __init__(self, dataProviderSource, dataProviderConfiguration):
        self.dataProviderSource = dataProviderSource
        self.dataProviderConfiguration = dataProviderConfiguration
        print(self.dataProviderConfiguration.getConfiguration())
        asyncio.get_event_loop().run_until_complete(self.handler())
    
    async def handler(self):
        async with websockets.connect(f'ws://{self.dataProviderSource.value}:8765') as websocket:
            # set initial configuration
            await websocket.send(self.dataProviderConfiguration.getConfiguration())
            self.data = await websocket.recv()
    
    def getData(self):
        return json.loads(self.data)
            

class DataProviderSource(Enum):
    SIMULATION = "130.82.239.210"
    REAL = "192.168.8.10"

class DataProviderConfiguration:
    
    def __init__(self, signals, samplerate, withtimestamp):
        self.signals = signals
        self.samplerate = samplerate
        self.withtimestamp = withtimestamp
    
    def getConfiguration(self):
        return json.dumps({'signals': self.signals, 'samplerate': self.samplerate, 'withtimestamp': self.withtimestamp})