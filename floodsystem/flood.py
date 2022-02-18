#from floodsystem.station import MonitoringStation
#from floodsystem.stationdata import build_station_list

def stations_level_over_threshold(stations, tol):
    '''Returns a list of tuples which gives a station where
    the latest relative water level is over tol and that relative water level.
    Sorted in descending order'''
    overTol = [] # Empty list for tuples 
    for station in stations:
        if station.relative_water_level() == None:
            pass
        elif station.relative_water_level() > tol:
            tuple1 = (station,station.relative_water_level())
            overTol.append(tuple1)
        overTol.sort(key=lambda x: x[1], reverse=True)
    return overTol

def stations_highest_rel_level(stations, N):
    '''Returns the top N tuples for highest water level ratio
    which has staion object and water level ratio in. In descending order'''
    atRisk = [] # Empty list for tuples 
    for station in stations:
        if station.relative_water_level() == None:
            pass
        else:
            tuple1 = (station,station.relative_water_level())
            atRisk.append(tuple1)
        atRisk.sort(key=lambda x: x[1], reverse=True)
    nAtRisk = atRisk[0:N]
    return nAtRisk


        
