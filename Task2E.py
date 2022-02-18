from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib as mpl
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level


stations = build_station_list()
update_water_levels(stations)


five_riskiest_stations = stations_highest_rel_level(stations, 5)

for station in five_riskiest_stations:
    dates, levels = fetch_measure_levels(station.measure_id, dt = timedelta(days =10))
    plot_water_levels(station, dates, levels)

