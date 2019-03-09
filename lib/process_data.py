import pandas as pd
import numpy as np
import time
import json

def get_speed(dataProvider):
    r = dataProvider.getSpeed().payload
    r = r.decode("utf-8")
    print(r)
    return json.loads(r)['value']

def get_acceleration(dataProvider):
    r = dataProvider.getAccel().payload
    r = r.decode("utf-8")
    return json.loads(r)['value']

def get_breakPres(dataProvider):
    r = dataProvider.getBreakePress().payload
    r = r.decode("utf-8")
    return json.loads(r)['value']

# def process_data(dataProvider, datavisualizer):
#     max_speed = get_speed(dataProvider)
#     print(max_speed)
#     acceleration = get_acceleration(dataProvider)
#     acceleration_seq = []
#     speed_seq = []
#     breakPres_seq = []
#     if acceleration < 0:
#         while(acceleration < 0):
#             acceleration = get_acceleration(dataProvider)
#             acceleration_seq.append(acceleration)
#             speed_seq.append(get_speed(dataProvider))
#             # breakPres_seq.append(get_breakPres(dataProvider))
#
#         break_sequence = pd.DataFrame([acceleration_seq, speed_seq, breakPres_seq])
#         cur_speed = get_speed(dataProvider)
#         print(cur_speed , max_speed)
#         if cur_speed < max_speed-4:
#             datavisualizer.pushDataset(break_sequence[0])
#             print(break_sequence[0])

def process_data(dataProvider, datavisualizer):
    time.sleep(np.random.randint(1,15))
    max_speed = np.random.randint(20,80)
    n_timestamps = np.random.randint(50,200)
    optimal = []
    speed = max_speed
    for i in range(n_timestamps):
        optimal.append(speed)
        speed -= max_speed/n_timestamps

    df = pd.DataFrame(optimal, columns=['optimal'])
    df['actual'] = df['optimal'] + (3*np.random.rand(df.shape[0]))
    datavisualizer.pushDataset(df.to_json())
    print('pushDataset')