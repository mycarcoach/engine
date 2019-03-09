#!/usr/bin/env python
from enum import Enum
import json
import queue
import threading
import paho.mqtt.client as mqtt

# must be here because of the shitty library design of paho-mqtt
speedQueue = queue.Queue()
accelQueue = queue.Queue()
breakePressQueue = queue.Queue()
signals = ["ESP_v_Signal", "ESP_Laengsbeschl", "ESP_Bremsdruck"]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    for signal in signals:
        print(f"subscribing to /signal/{signal}")
        client.subscribe(f"/signal/{signal}")

def on_message(client, userdata, msg):
    if "/signal/ESP_v_Signal"== msg.topic:
        speedQueue.put(msg)
    elif "/signal/ESP_Laengsbeschl" == msg.topic:
        accelQueue.put(msg)
    elif "/signal/ESP_Bremsdruck" == msg.topic:
        breakePressQueue.put(msg)
    else:
        print("other topic")


# provides the data acquired from the websocket server
class DataProvider():

    def __init__(self):

        self.t = threading.Thread(target=self.inputThread)
        self.t.start()

    def inputThread(self):
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("46.101.168.60", 1883, 60)
        client.loop_forever()

    def getSpeed(self):
        return speedQueue.get()

    def getAccel(self):
        return accelQueue.get()

    def getBreakePress(self):
        return breakePressQueue.get()

    def getSpeedSize(self):
        return speedQueue.qsize()

    def accelQueueSize(self):
        return accelQueue.qsize()

    def breakePressQueueSize(self):
        return breakePressQueue.qsize()
