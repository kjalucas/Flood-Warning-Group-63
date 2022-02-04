from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list


def test_riverFunction():
    stations = build_station_list()
    return rivers_with_station(stations)

print(test_riverFunction())