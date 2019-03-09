import asyncio
import datetime
import random
from websocket_server import WebsocketServer
import threading
import queue
import time

client = None

def new_client(newClient, server):
    client = newClient
    server.send_message_to_all("Hey all, a new client has joined us")

class DataVisualizer:

    def __init__(self):
        self.dataQueue = queue.Queue()
        t = threading.Thread(target=self.thread)
        t.start()

    def pushDataset(self, data):
        self.dataQueue.put(data)

    def thread(self):
        server = WebsocketServer(7254, host='127.0.0.1')
        # server.send_message('127.0.0.1', )
        server.set_fn_new_client(new_client)

        server.run_forever()
