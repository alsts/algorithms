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


# Shortest path in adjacency list
def bfs(start, finish, adj_list):
    visited = set()
    queue = deque()
    visited.add(start)
    queue.append(start)
    path_count = 0

    while queue:
        curr = queue.popleft()
        if curr == finish:
            return path_count

        for vertex in adj_list[curr]:
            if vertex not in visited:
                queue.append(vertex)
                visited.add(vertex)

        path_count += 1

    return path_count


edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
al = adj_list(edges)
print(bfs("A", "E", al))
