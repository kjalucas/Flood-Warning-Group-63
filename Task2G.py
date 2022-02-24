from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib as mpl
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from collections import Counter
from floodsystem.station import MonitoringStation


stations = build_station_list()
update_water_levels(stations)
station_names = []

dictionary = {}

for station in stations:
    if station.town in station_names:
        pass
    else:
        station_names.append(station.town)



for station in stations:
    level = station.relative_water_level()
    if level == None:
        break
    town = station.town
    if level < 0.8:
        if town in dictionary:
            dictionary[town].append(1)
        else:
            dictionary[town] = [1]
    elif 0.8 <= level <= 1.2:
        if town in dictionary:
            dictionary[town].append(2)
        else:
            dictionary[town] = [2]



dictionary["Ardingly"].append(1)

print(dictionary)