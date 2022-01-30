from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

stations = build_station_list()

names = []

for station in stations:
    data =station.name
    names.append(data)

inconsistent_stations = sorted(inconsistent_typical_range_stations(stations))
print(inconsistent_stations)


