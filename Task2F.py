from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib as mpl
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.plot import plot_water_level_with_fit
import matplotlib.dates as date

#make a random list of stations to use until Sophie does the first parts
stations = build_station_list()
five_riskiest_stations = stations[0:1]
## need to add in code that selects the five riskiest stations
## edit stations[0:1] to [0:5] after all code is written

for station in five_riskiest_stations:
    dates, levels = fetch_measure_levels(station.measure_id, dt = timedelta(days =2))
    print(len(dates), len(levels))
    dates = date.date2num(dates)
    plot_water_level_with_fit(station, dates, levels, 4)

    