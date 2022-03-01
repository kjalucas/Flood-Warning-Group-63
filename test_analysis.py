from re import L
import numpy as np
import matplotlib as mpl
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit

def test_polyfit():
    dates = mpl.dates.num2date([1,2,3,4,5])
    levels = [1,8,27,64,125]
    d0, poly = polyfit(dates, levels, 3)
    assert d0 == 1
    assert round(poly[3]) == 1
