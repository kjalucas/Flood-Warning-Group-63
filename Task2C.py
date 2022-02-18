from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
#from Task2B import names_and_levels

def names_and_levels(tuples): 
    '''Creates a list of tuples with station names and water level ratios from a list 
    of station objects and water level ratios '''
    newList = []
    for t in tuples:
        newTuple = (t[0].name,t[1])    
        newList.append(newTuple)
    return newList 

stations = build_station_list()
update_water_levels(stations)
s = stations_highest_rel_level(stations, 10)

print(names_and_levels(s))
