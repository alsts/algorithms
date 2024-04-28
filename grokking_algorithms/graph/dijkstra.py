graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}

table = {
    "a": {"parent": "start", "cost": 6, "visited": False},
    "b": {"parent": "start", "cost": 2, "visited": False},
    "fin": {"parent": None, "cost": float("inf"), "visited": False}
}


def find_lowest_cost_node_key(table_arr):
    lowest_cost = float("inf")
    lowest_cost_node_key = None

    for node_key, node in table_arr.items():
        if not node["visited"] and node["cost"] < lowest_cost:
            lowest_cost = node["cost"]
            lowest_cost_node_key = node_key

    return lowest_cost_node_key


def dijkstra():
    node_key = find_lowest_cost_node_key(table)
    while node_key is not None:

        node_cost_from_start = table[node_key]["cost"]
        node_neighbors = graph[node_key]

        for neighbour_key, neighbour_cost in node_neighbors.items():
            neighbour_new_cost_from_start = node_cost_from_start + neighbour_cost

            if neighbour_new_cost_from_start < table[neighbour_key]["cost"]:
                table[neighbour_key]["cost"] = neighbour_new_cost_from_start
                table[neighbour_key]["parent"] = node_key

        table[node_key]["visited"] = True
        node_key = find_lowest_cost_node_key(table)


dijkstra()
# print(costs)
