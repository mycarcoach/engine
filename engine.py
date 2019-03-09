#!/usr/bin/env python
from lib import dataprovider

import time

def main():
    dataProviderSource = dataprovider.DataProviderSource.SIMULATION
    dataProvider = dataprovider.DataProvider(dataProviderSource)
    
    while 1:
        print(dataProvider.getSpeedSize())
        print(dataProvider.accelQueueSize())
        print(dataProvider.breakePressQueueSize())
        time.sleep(0.05)

if __name__ == "__main__":
    main()