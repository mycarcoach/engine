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
        self.data = '{ "foo": "bar" }'

    async def handler(self):
        async with websockets.connect('ws://130.82.239.210/ws') as websocket:
            print("Inside socket")
            # set initial configuration
            await websocket.send(self.dataProviderConfiguration.getConfiguration())
            print(f"data sent: {self.dataProviderConfiguration.getConfiguration()}")
            await asyncio.sleep(1)
            try:
                self.data = await websocket.recv()
            except asyncio.streams.IncompleteReadError:
                pass
            except websockets.exceptions.ConnectionClosed:
                pass
            else:
                print("Data returned:")
                print(self.data)
            finally:
                print("The 'try except' is finished")

    def getData(self):
        asyncio.get_event_loop().
        asyncio.get_event_loop().run_until_complete(self.handler())
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