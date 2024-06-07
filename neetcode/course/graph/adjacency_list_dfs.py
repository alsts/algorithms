from collections import deque


def adj_list(edges):
    adjacency_list = {}

    for src, dst in edges:
        # Initialise both src and dst nodes if not present:
        if src not in adjacency_list:
            adjacency_list[src] = []
        if dst not in adjacency_list:
            adjacency_list[dst] = []

        adjacency_list[src].append(dst)

    return adjacency_list


# All paths   to node in adjacency list
def dfs(node, finish, adj_list, visited):
    if node == finish:
        return 1
    if node in visited:
        return 0

    path_count = 0
    visited.add(node)
    for neighbour in adj_list[node]:
        path_count += dfs(neighbour, finish, adj_list, visited)
    visited.remove(node)

    return path_count


edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
al = adj_list(edges)
print(dfs("A", "E", al, set()))
