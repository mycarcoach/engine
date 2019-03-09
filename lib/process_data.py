import pandas as pd
import numpy as np
import time
import json
import matplotlib.pyplot as plt

def get_speed(dataProvider):
    r = dataProvider.getSpeed().payload
    r = r.decode("utf-8")
    return json.loads(r)['value']

def get_acceleration(dataProvider):
    r = dataProvider.getAccel().payload
    r = r.decode("utf-8")
    return json.loads(r)['value']

def get_breakPres(dataProvider):
    r = dataProvider.getBreakePress().payload
    r = r.decode("utf-8")
    return json.loads(r)['value']

def process_data(dataProvider, datavisualizer):
    testplot_count = 0
    while True:
        time.sleep(0.5)
        start_speed = get_speed(dataProvider)
        acceleration = get_acceleration(dataProvider)
        acceleration_seq = []
        speed_seq = [start_speed]
        # breakPres_seq = []
        current_speed = start_speed
        prev_speed = current_speed
        if acceleration < 0:
            while(acceleration < 0.2 and current_speed > 0.1):
                current_speed = get_speed(dataProvider)
                speed_seq.append(current_speed)
                acceleration = get_acceleration(dataProvider)
                acceleration_seq.append(acceleration)
                # breakPres_seq.append(get_breakPres(dataProvider))

            optimal = []
            speed = start_speed
            end_speed = current_speed
            for i in range(len(speed_seq)):
                    optimal.append(speed)
                    speed -= (start_speed-end_speed)/len(speed_seq)

            print('\n',len(optimal))
            break_sequence = pd.DataFrame([optimal, speed_seq],
                                          index=[ 'optimal', 'actual']).T
            cur_speed = get_speed(dataProvider)
            print(start_speed, cur_speed)
            if cur_speed < start_speed-4:
                # datavisualizer.pushDataset(break_sequence.to_json())
                print('save img')
                break_sequence.plot(subplots=True)
                plt.savefig('testplot{}.png'.format(testplot_count))
                testplot_count += 1


# def process_data(dataProvider, datavisualizer):
#     time.sleep(np.random.randint(1,15))
#     start_speed = np.random.randint(20,80)
#     n_timestamps = np.random.randint(50,200)
#     optimal = []
#     speed = start_speed
#     for i in range(n_timestamps):
#         optimal.append(speed)
#         speed -= start_speed/n_timestamps
#
#     df = pd.DataFrame(optimal, columns=['optimal'])
#     df['actual'] = df['optimal'] + (3*np.random.rand(df.shape[0]))
#     datavisualizer.pushDataset(df.to_json())
#     print(df.to_json())
