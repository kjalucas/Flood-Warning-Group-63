import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation


def plot_water_levels(station, dates, levels):

    # Plot
    plt.plot(dates, levels)

    #Plot low range
    plt.plot([dates[0], dates [-1]], [station.typical_range[0], station.typical_range[0]], label="Typical Low Levels")

    #Plot high range
    plt.plot([dates[0], dates [-1]], [station.typical_range[1], station.typical_range[1]], label="Typical High Levels")



    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station " + station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
