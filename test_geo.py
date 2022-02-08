from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius

def test_stations_by_distance():

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

    stations = [a,c,b]
    distances = stations_by_distance(stations, (0, 0))
    stations_and_distances = []
    for station, distance in distances:
        data = [station.name, distance]
        stations_and_distances.append(data)

    assert stations_and_distances[1][0] == "Station 2"
    

def test_stations_within_radius():

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

    stations = [a,c,b]
    in_radius = stations_within_radius(stations, (0,0), 400)
    stations_in_radius = []

    for station, distance in in_radius:
        data = station.name
        stations_in_radius.append(data)
        
    assert len(stations_in_radius) == 2 





    