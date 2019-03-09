import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("CONNECTED!")
    
client = mqtt.Client()
client.on_connect = on_connect
client.connect("46.101.168.60", 1883, 60)
client.loop_start()

f = open("/Users/eliabieri/Downloads/testDrive.csv")
for line in f.readlines():
    if line.startswith(","):
            #skip first line
        continue
    values = line.split(",")
    client.publish("/value/ESP_v_Signal", values[1], qos=0, retain=False)
    client.publish("/value/ESP_Bremsdruck", values[2], qos=0, retain=False)
    client.publish("/value/ESP_Laengsbeschl", values[3], qos=0, retain=False)
    time.sleep(0.01)

client.loop_stop()