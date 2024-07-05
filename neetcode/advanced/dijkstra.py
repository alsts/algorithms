import heapq


# Given a connected graph represented by a list of edges, where
# edge[0] = src, edge[1] = dst, and edge[2] = weight,
# find the shortest path from src to every other node in the graph.
# There are n nodes in the graph.
# Time Complexity: O(E * logV), O(E * logE) is also correct.
def dijkstra(adj, start):
    visited = {}
    min_heap = [(0, start, None)]

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)  # take min weight node

        if node in visited:  # skip duplicated entries (higher weights)
            print("Node skipped: " + node + " with parent: " + parent)
            continue

        visited[node] = (weight, parent)  # mark visited -> 100% lowest weight

        for child_node, child_weight in adj[node]:
            if child_node not in visited:
                heapq.heappush(min_heap, (weight + child_weight, child_node, node))

    return visited


edges = [
    ['A', 'C', 3],
    ['A', 'B', 10],
    ['C', 'B', 4],
    ['C', 'D', 8],
    ['C', 'E', 2],
    ['B', 'D', 2],
    ['D', 'E', 5],
]

adj = {}

for src, dst, weight in edges:
    if src not in adj:
        adj[src] = []
    if dst not in adj:
        adj[dst] = []

    adj[src].append((dst, weight))

print(dijkstra(adj, 'A'))
