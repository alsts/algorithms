# Given a directed acyclical graph, return a valid
# topological ordering of the graph.
def topological_sort(adj):
    result = []
    visited = set()

    # Apply DFS Post Order on
    for node in adj:
        dfs(node, adj, visited, result)

    # Reverse Result
    result.reverse()
    return result


def dfs(src, adj, visited, result):
    if src in visited:
        return

    visited.add(src)

    # Append all neighbour nodes to result first (Post Order)
    for neighbour in adj[src]:
        dfs(neighbour, adj, visited, result)

    # Add node to result
    result.append(src)


# Test Data:
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'E'),
    ('D', 'F'),
    ('E', 'F'),
    ('G', 'H'),
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
