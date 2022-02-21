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


stations = build_station_list()
update_water_levels(stations)

flooded_list_x = stations_highest_rel_level(stations, 10)

flooded_list = []

for station in stations:
    for i in range(4,9):
        if (flooded_list_x[i][0]).name == station.name:
            flooded_list.append(station)


for station in flooded_list:
    dates, levels = fetch_measure_levels(station.measure_id, dt = timedelta(days = 2))    
    plot_water_level_with_fit(station,dates,levels, 4)



    