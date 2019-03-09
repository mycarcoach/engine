import asyncio
import datetime
import random
import websockets
import threading
import queue

class DataVisualizer:
    
    def __init__(self):
        self.dataQueue = queue.Queue()
        t = threading.Thread(target=self.thread)
        t.start()
        
    def pushDataset(self, data):
        self.dataQueue.put(data)
    
    def thread(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        start_server = websockets.serve(self.visualProvider, '127.0.0.1', 5678)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
        

    async def visualProvider(websocket, path):
        while True:
            if not self.dataQueue.empty():
                await websocket.send(self.dataQueue.get())
            await asyncio.sleep(0.1)

