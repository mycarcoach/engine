import asyncio
import datetime
import random
from websocket_server import WebsocketServer
import threading
import queue
import time

dataQueue = queue.Queue()

def new_client(newClient, server):

    while True:
        try:
            if not dataQueue.empty():
                server.send_message(newClient, dataQueue.get())
                print(f'>>>>>> pushde new data to frontend. Current queue size {dataQueue.qsize()}')
            time.sleep(0.05)
        except:
            print("pipe is broken -> reconnecting")

class DataVisualizer:

    def __init__(self):
        t = threading.Thread(target=self.thread)
        t.start()

    def pushDataset(self, data):
        dataQueue.put(data)
        print(f"Push request for new dataset. Current queue size {dataQueue.qsize()}")

    def thread(self):
        while 1:
            server = WebsocketServer(7254, host='127.0.0.1')
            server.set_fn_new_client(new_client)

            server.run_forever()
