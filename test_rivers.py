from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

def test_riverFunction():
    stations = build_station_list()
    return list(rivers_with_station(stations))

print("Printing list of rivers",test_riverFunction()[0:10])

def test_riverDictFunction():
    stations = build_station_list()
    items = list(stations_by_river(stations).items())
    return items[0:10]

print("Printing Dictionary of rivers with their stations",test_riverDictFunction())
