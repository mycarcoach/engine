#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data/first_drive.csv')

df.shape
df.columns.values
df.values

cols = ['can0_ESP_HL_Radgeschw_02 [Unit_KiloMeterPerHour]',
        'can0_ESP_HR_Radgeschw_02 [Unit_KiloMeterPerHour]',
        'can0_ESP_VL_Radgeschw_02 [Unit_KiloMeterPerHour]',
        'can0_ESP_VR_Radgeschw_02 [Unit_KiloMeterPerHour]']

df['avg_speed [Unit_KiloMeterPerHour]'] = df.loc[:, cols].sum(axis=1) / 4

df.loc[:, cols].plot(figsize=(20,12), kind="line")

cols = ['can0_ESP_v_Signal [Unit_KiloMeterPerHour]',
        'can0_ESP_Bremsdruck [Unit_Bar]',
        'can0_ESP_Laengsbeschl [Unit_MeterPerSeconSquar]']

ax = df.loc[:, cols].plot(figsize=(20, 12), subplots=True)
#%%
plt.savefig('speed.png')


ax = df.loc[:, cols].plot(figsize=(20, 8))
plt.savefig('speed_onePlot.png')
