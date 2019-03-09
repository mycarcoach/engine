#!/usr/bin/env python
from lib import dataprovider
from lib import process_data
from lib import datavisualizer

import time

def main():
    dataProviderSource = dataprovider.DataProviderSource.SIMULATION
    dataProvider = dataprovider.DataProvider(dataProviderSource)
    
    visualizer = datavisualizer.DataVisualizer()

    while 1:
        process_data.process_data(dataProvider, visualizer)

if __name__ == "__main__":
    main()
