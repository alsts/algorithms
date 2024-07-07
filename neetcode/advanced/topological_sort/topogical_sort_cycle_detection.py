# Given a graph, return a valid topological ordering of the graph.
def topological_sort(adj):
    result = []
    visited = set()
    path = set()

    # Apply DFS Post Order on
    for node in adj:
        if dfs(node, adj, visited, result, path) is False:
            return -1

    # Reverse Result
    result.reverse()
    return result


def dfs(src, adj, visited, result, path):
    if src in path:
        print("Cycle detected at: " + src + " Topological Oder can not be produced")
        return False  # cycle detected!!!

    if src in visited:
        return True

    visited.add(src)
    path.add(src)  # Append to current path

    # Append all neighbour nodes to result first (Post Order)
    for neighbour in adj[src]:
        if dfs(neighbour, adj, visited, result, path) is False:
            return False

    # Add node to result
    result.append(src)
    # Clean Up for backtracking
    path.remove(src)


# Test Data:
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'E'),
    ('D', 'F'),
    ('E', 'F'),
    ('G', 'H'),
    ('C', 'A'),
]

# Build adjacency list:
adj = {}
for src, dst in edges:
    if src not in adj:
        adj[src] = []
    if dst not in adj:
        adj[dst] = []

    adj[src].append(dst)

print(topological_sort(adj))
