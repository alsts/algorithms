stations = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"}
}

states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
final_stations = set()

while states_needed:
    best_station = None
    best_station_covered_intersection = set()

    for station, station_states in stations.items():
        station_covered_intersection = states_needed & station_states  # intersection

        if len(station_covered_intersection) > len(best_station_covered_intersection):
            best_station = station
            best_station_covered_intersection = station_covered_intersection

    states_needed -= best_station_covered_intersection
    final_stations.add(best_station)

print(final_stations)
