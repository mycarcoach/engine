import asyncio
import datetime
import random
import websocket
import threading
import queue
import time

class DataVisualizer:
    
    def __init__(self):
        self.dataQueue = queue.Queue()
        t = threading.Thread(target=self.thread)
        t.start()
        
    def pushDataset(self, data):
        self.dataQueue.put(data)
    
    def thread(self):
        print("Starting visualizer thread...")
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("ws://127.0.0.0:5678",
                              on_open=self.on_open)
        ws.run_forever()
    
    def on_open(self, ws):
        while True:
            if not self.dataQueue.empty():
                print("pushed data to ws client")
                ws.send(self.dataQueue.get())
            time.sleep(0.1)
