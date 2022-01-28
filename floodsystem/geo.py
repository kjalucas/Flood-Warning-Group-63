# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    distance_list = []
    for station in stations:
        distance = haversine(station.coord, p)
        distance_list.append((station, distance))
    return sorted_by_key(distance_list, 1)



def stations_within_radius(stations, centre, r):
    within_radius = []
    for station in stations:
        location = station.coord()
        distance_from_x = haversine(location, centre)
        if distance_from_x <= r:
            within_radius.append(station)

    return within_radius
