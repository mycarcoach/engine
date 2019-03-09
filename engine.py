#!/usr/bin/env python
from lib import dataprovider
from lib import process_data
from lib import datavisualizer

import time

def main():
    dataProvider = dataprovider.DataProvider()
    
    visualizer = datavisualizer.DataVisualizer()

    process_data.process_data(dataProvider, visualizer)

if __name__ == "__main__":
    main()
