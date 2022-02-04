from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

stations = build_station_list()

list_in_radius = stations_within_radius(stations, (52.2053, 0.1218), 10)
new_list = []

for station, distance in list_in_radius:
    data =station.name
    new_list.append(data)

alphabetical_list = sorted(new_list)

print("Stations within a 10km radius of Cambridge:", alphabetical_list ,"\n")


