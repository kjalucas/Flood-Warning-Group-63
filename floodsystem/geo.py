# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list

def stations_by_distance(stations, p):
    distance_list = []
    for station in stations:
        distance = haversine(station.coord, p)
        distance_list.append((station, distance))
    return sorted_by_key(distance_list, 1)



def stations_within_radius(stations, centre, r):
    within_radius = []
    distance_list = stations_by_distance(stations,centre)
    for station in distance_list:
        if station[1] <= r:
            within_radius.append(station)

    return within_radius

def rivers_with_station(stations):
    """Create's a list of rivers from a list of Monitoring Stations"""
    RiversSet = set()
    for station in stations:
        RiversSet.add(station.river)
    
    return RiversSet

def stations_by_river(stations):
    """Create's a dictionary of all the rivers as the keys and the stations that monitor
    them as their values"""
    riverDict = {}
    ListOfRivers = list(rivers_with_station(stations))
    for r in ListOfRivers:
        rStations = []
        for s in stations:
            if s.river == r:
                rStations.append(s)
        riverDict[r] = rStations
    
    return riverDict

def rivers_by_station_number(stations, N):
    tuples = []
    riverDict = stations_by_river(stations)
    for i in range(N):
        x=0
        for key in riverDict.keys():
            l = len(riverDict[key])
            if l > x:
                x = l
                tuple1 = (key,l)
                highestKey = key
        tuples.append(tuple1)
        print(highestKey)
        riverDict.pop(highestKey)      
    for key in riverDict.keys():
            l = len(riverDict[key])
            if l == x:
                tuple2 = (key,l)
                tuples.append(tuple2)
    return tuples  

