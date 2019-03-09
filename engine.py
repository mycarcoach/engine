#!/usr/bin/env python
import dataprovider

if __name__ == "__main__":
    dataProviderSource = dataprovider.DataProviderSource.SIMULATION
    dataProviderConfiguration = dataprovider.DataProviderConfiguration(["MO_Drehzahl_01"], 250, True)
    dataProvider = dataprovider.DataProvider(dataProviderSource, dataProviderConfiguration)
    while 1:
        print(dataProvider.getData())
