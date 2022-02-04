from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

stations = build_station_list()
distances = stations_by_distance(stations, (52.2053, 0.1218))

stations_and_distances = []

for station, distance in distances:
    data = [station.name, station.town, distance]
    stations_and_distances.append(data)

ten_closest = stations_and_distances[:10]
ten_furthest = stations_and_distances[-10:]
print("Ten stations closest to co-ordinate:", ten_closest ,"\n")
print("Ten stations furthest from co-ordinate:", ten_furthest ,"\n")
