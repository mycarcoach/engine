import pandas as pd
from os import listdir

print(pd.__version__)

# get list of files
files = pd.Series(listdir())
files = files.loc[files.str.endswith('.csv')]

# %% concat data
df = pd.DataFrame()
for unique_time in files.str.split('_DataGroup_', expand=True)[0].unique():
    if files.loc[files.str.startswith(unique_time)].shape[0] != 18:
        print('group not complete. Timestamp: ', unique_time)
        continue

    DataGroup = pd.DataFrame()
    for i in range(1,19):
        part = pd.read_csv('{}_DataGroup_{}.csv'.format(unique_time, i))
        part['time'] = part.time.round(decimals=2)
#        DataGroup = pd.concat([DataGroup, part], sort=False, axis=1)
        if i ==1:
            DataGroup = part
        DataGroup = DataGroup.merge(part, how='outer', on='time')
        DataGroup = DataGroup.sort_values('time')
        DataGroup = DataGroup.fillna(method='ffill', axis=0)

    if 'can1_ND_UTC [Unit_Secon]' not in DataGroup.columns:
        print('no timestamp', unique_time)
        continue

    DataGroup['Timestamp'] = DataGroup['can1_ND_UTC [Unit_Secon]'].astype('str') + DataGroup.time.astype('str')
    df = df.append(DataGroup, sort=False)

df.shape
df.to_csv('first_drive.csv')
df.to_pickle('first_drive.pkl')