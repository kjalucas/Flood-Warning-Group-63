from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

stationsTestE = build_station_list()
print(rivers_by_station_number(stationsTestE, 2))
