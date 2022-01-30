from sympy import inverse_cosine_transform
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

stations = build_station_list()



inconsistent_stations = (inconsistent_typical_range_stations(stations))

names = []
for station in inconsistent_stations:
    s = station.name
    names.append(s)

alphabetical_names = sorted(names)



print(alphabetical_names)


