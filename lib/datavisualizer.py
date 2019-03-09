import asyncio
import datetime
import random
from websocket_server import WebsocketServer
import threading
import queue
import time

dataQueue = queue.Queue()

def new_client(newClient, server):
    client = newClient
    server.send_message_to_all("Connection established")

    while True:
        if not dataQueue.empty():
            print('>>>>>> push new data to frontend')
            server.send_message(newClient, dataQueue.get())
        time.sleep(0.05)

class DataVisualizer:

    def __init__(self):
        t = threading.Thread(target=self.thread)
        t.start()

    def pushDataset(self, data):
        dataQueue.put(data)

    def thread(self):
        server = WebsocketServer(7254, host='127.0.0.1')
        server.set_fn_new_client(new_client)

        server.run_forever()
