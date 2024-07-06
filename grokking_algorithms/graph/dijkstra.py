graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}

shortest = {
    "a": {"parent": "start", "cost": 6, "visited": False},
    "b": {"parent": "start", "cost": 2, "visited": False},
    "fin": {"parent": None, "cost": float("inf"), "visited": False}
}


# Time Complexity: O(n)
def find_lowest_cost_node_key(table_arr):
    lowest_cost = float("inf")  # max possible value
    lowest_cost_node_key = None

    for node_key, node in table_arr.items():
        if not node["visited"] and node["cost"] < lowest_cost:
            lowest_cost = node["cost"]
            lowest_cost_node_key = node_key

    return lowest_cost_node_key


def dijkstra():
    node_key = find_lowest_cost_node_key(shortest)
    while node_key is not None:
        for neighbour_key, neighbour_cost in graph[node_key].items():
            node_cost_from_start = shortest[node_key]["cost"]
            neighbour_new_cost_from_start = node_cost_from_start + neighbour_cost

            # Override node cost and parent if lower: (It would never override if cost higher)
            if neighbour_new_cost_from_start < shortest[neighbour_key]["cost"]:
                shortest[neighbour_key]["cost"] = neighbour_new_cost_from_start
                shortest[neighbour_key]["parent"] = node_key

        shortest[node_key]["visited"] = True
        node_key = find_lowest_cost_node_key(shortest)


dijkstra()
print(shortest)
