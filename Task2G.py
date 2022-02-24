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
town_means = {}

for station in stations:
    town = station.town
    if town in dictionary:
        dictionary[town].append(station)
    else:
        dictionary[town] = [station]

for station in stations:
    town = station.town
    if town in town_means:
        town_means[town].append(station)
    else:
        town_means[town] = [station]

for town in dictionary:
    level_list = []
    for station in dictionary[town]:
        level = station.relative_water_level()
        if level != None:
            level_list.append(level)
    if len(level_list) != 0:
        mean = sum(level_list)/len(level_list)
        town_means[town] = mean
    else:
        town_means[town] = 0

not_risky = []
low = []
moderate = []
high = []
severe = []

for town in town_means:
    if town_means[town] < 1.2:
        not_risky.append(town)

    elif town_means[town] < 1.5:
        low.append(town)

    elif town_means[town] < 1.8:
        moderate.append(town)
    
    elif town_means[town] < 2.1:
        high.append(town)

    else:
        severe.append(town)

print(severe)