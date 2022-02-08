from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius
from floodsystem.station import inconsistent_typical_range_stations

def test_stations_by_distance():

    ## create a set of three imaginary stations

    s_id = "test-s-id"
    m_id = "test-m-id"
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    


    label1 = "Station 1"
    coord1 = (1,1)
    a = MonitoringStation(s_id, m_id, label1, coord1, trange, river, town)
    
    label2 = "Station 2"
    coord2 = (2,2)
    b = MonitoringStation(s_id, m_id, label2, coord2, trange, river, town)

    label3 = "Station 3"
    coord3 = (3,3)
    c = MonitoringStation(s_id, m_id, label3, coord3, trange, river, town)

    ## put the stations in a list

    stations = [a,c,b]

    ## test that the function returns a list of objects in order a,b,c

    distances = stations_by_distance(stations, (0, 0))
    stations_and_distances = []
    for station, distance in distances:
        data = [station.name, distance]
        stations_and_distances.append(data)

    assert stations_and_distances[1][0] == "Station 2"
    

def test_stations_within_radius():

    ## create a set of three imaginary stations

    s_id = "test-s-id"
    m_id = "test-m-id"
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    


    label1 = "Station 1"
    coord1 = (1,1)
    a = MonitoringStation(s_id, m_id, label1, coord1, trange, river, town)
    
    label2 = "Station 2"
    coord2 = (2,2)
    b = MonitoringStation(s_id, m_id, label2, coord2, trange, river, town)

    label3 = "Station 3"
    coord3 = (3,3)
    c = MonitoringStation(s_id, m_id, label3, coord3, trange, river, town)

    ## put the stations in a list

    stations = [a,c,b]

    ## checking how many stations are within a radius of 400 - should be stations 1 and 2 with radius 100 and 314 respectively
    in_radius = stations_within_radius(stations, (0,0), 400)
    stations_in_radius = []

    for station, distance in in_radius:
        data = station.name
        stations_in_radius.append(data)
        
    assert len(stations_in_radius) == 2 

def test_inconsistent_typical_range_stations():

    ## create a set of three imaginary stations

    s_id = "test-s-id"
    m_id = "test-m-id"
    river = "River X"
    town = "My Town"
    


    label1 = "Station 1"
    coord1 = (1,1)
    trange1 = (2, -2)
    a = MonitoringStation(s_id, m_id, label1, coord1, trange1, river, town)
    
    label2 = "Station 2"
    coord2 = (2,2)
    trange2 = (3, 10)
    b = MonitoringStation(s_id, m_id, label2, coord2, trange2, river, town)

    label3 = "Station 3"
    coord3 = (3, 3)
    trange3 = (1, -1)
    c = MonitoringStation(s_id, m_id, label3, coord3, trange3, river, town)

    ## put the stations in a list

    stations = [a,c,b]

    ## tests function on stations and creates a list of inconsistent stations
    inconsistent_stations = (inconsistent_typical_range_stations(stations))
    names = []
    for station in inconsistent_stations:
        s = station.name
        names.append(s)

    ##check that names contains the two stations - 1 and 3 - that have inconsistent ranges

    assert len(names) == 2







    