from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

stations1D = build_station_list()
rivers = list(rivers_with_station(stations1D))
rivers.sort()
print(len(rivers)," Stations. First 10 - ",rivers[0:10],"\n")

riverDict = stations_by_river(stations1D)

def river_station_names(riverName):
    s = riverDict[riverName]
    names = []
    for i in s:
        names.append(i.name)
    names.sort()
    return names

print("Stations located on the River Aire ",river_station_names("River Aire"),"\n")
print("Stations located on the River Cam ",river_station_names("River Cam"),"\n")
print("Stations located on the River Thames ",river_station_names("River Thames"),"\n")


