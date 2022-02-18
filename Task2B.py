from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


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
s = stations_level_over_threshold(stations, 0.8)

def tuplesInLines(listOfTuples):
    for i in range(len(listOfTuples)):
        print(listOfTuples[i][0],listOfTuples[i][1])
        

f = names_and_levels(s)
tuplesInLines(f)