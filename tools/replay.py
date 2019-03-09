import paho.mqtt.client as mqtt
import time
import json
def main():
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
        speed = json.dumps('{"signal":{"definition":{"name":"speed","unit":"Unit_PerCent","description":"in km/h"},"measurement":{"value":{' + values[1] + '},"utc":1550761385086735000}}')
        break_ = json.dumps('{"signal":{"definition":{"name":"speed","unit":"Unit_PerCent","description":"in km/h"},"measurement":{"value":{' + values[2] + '},"utc":1550761385086735000}}')
        accel = json.dumps('{"signal":{"definition":{"name":"speed","unit":"Unit_PerCent","description":"in km/h"},"measurement":{"value":{' + values[3] + '},"utc":1550761385086735000}}')
        client.publish("/value/ESP_v_Signal", speed, qos=0, retain=False)
        client.publish("/value/ESP_Bremsdruck", break_, qos=0, retain=False)
        client.publish("/value/ESP_Laengsbeschl", accel, qos=0, retain=False)
        time.sleep(0.01)
    
    client.loop_stop()

if __name__=="__main__":
    main()