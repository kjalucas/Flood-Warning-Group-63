from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

stations1E = build_station_list()
print("Rivers with the most stations: ",rivers_by_station_number(stations1E, 9))