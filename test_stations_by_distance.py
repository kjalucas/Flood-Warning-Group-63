from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation

if 1 ==1 :

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

    assert stations_and_distances[1][0] == "Station 2":
    





    


