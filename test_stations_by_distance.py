from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def test_stations_by_distance():
    stations = build_station_list()
    distances = stations_by_distance(stations, (52.2053, 0.1218))
    assert len(stations) == len(distances)
    return distances

print("Printing stations close to Cambridge",test_stations_by_distance()[:10])




    


