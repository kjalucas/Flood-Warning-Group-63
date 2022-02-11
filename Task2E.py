from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib as mpl
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels


#make a random list of stations to use until Sophie does the first parts
stations = build_station_list()
five_stations = stations[0:5]
print(five_stations)

