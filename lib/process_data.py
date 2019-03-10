import pandas as pd
import numpy as np
import time
import json
# import matplotlib.pyplot as plt


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

def speed_from_accel(acceleration, high, low):
    speed = np.cumsum(acceleration)
    # scale
    speed *= (high-low) / (speed[0] - speed[-1])
    speed += high
    return speed

def calculate_optimal(accel_seq, delta_speed):
    n_steps = len(accel_seq)
    np.trapz(accel_seq)

    time = np.arange(0, np.pi, np.pi/(delta_speed*3.5))
    optimal = np.concatenate((np.cos(time),
                              -1*np.ones(n_steps-2*len(time)),
                              np.cos(time + np.pi)))*0.5-0.5
    optimal *= np.trapz(accel_seq) / np.trapz(optimal)
    return optimal


def process_data(dataProvider, datavisualizer):
    testplot_count = 0
    threshold = 12
    while True:
        start_speed = get_speed(dataProvider)
        speed_seq = [start_speed]
        accel_seq = [0]
        if get_acceleration(dataProvider) < 0:
            start = time.time()
            # record speed until it gets faster again
            # while ((len(speed_seq) < 11 or
            #        sum(speed_seq[-10:-5]) > sum(speed_seq[-5:])) and
            #        speed_seq[-1] > 0.1):
            while ((len(accel_seq) < 11 or
                   0 > sum(accel_seq[-5:])) and
                   sum(speed_seq[-3:]) > 0.1):
                speed_seq.append(get_speed(dataProvider))
                accel_seq.append(get_acceleration(dataProvider))

            delta_time = time.time()-start

            # stop iteration if speed difference is smaler than threshold
            if speed_seq[-1] > (speed_seq[0] - threshold):
                continue

            # define optimal curve
            optimal = calculate_optimal(accel_seq, speed_seq[0] - speed_seq[-1])
            print('trapz optimal', np.trapz(optimal))
            print('trapz actual', np.trapz(accel_seq))
            break_sequence = pd.DataFrame([optimal, accel_seq],
                                          index=['optimal', 'actual']).T

            datavisualizer.pushDataset(break_sequence.to_json())
            # print('save img')
            # break_sequence.plot(subplots=False)
            # plt.savefig('testplot{}.png'.format(testplot_count))
            # testplot_count += 1


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
