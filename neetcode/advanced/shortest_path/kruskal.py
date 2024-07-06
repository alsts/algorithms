# Given an list of edges of a connected undirected graph,
# with nodes numbered from 1 to n,
# return a list of edges making up the minimum spanning tree.
import heapq


class UnionFind:

    def __init__(self, nodes_count):
        self.parents = {}
        self.ranks = {}

        # fill each Tree height and parent Initial state
        for node in range(1, nodes_count + 1):
            self.parents[node] = node  # parent to itself (indicate that not have parent yet)
            self.ranks[node] = 0  # height of Tree is 0

    def find_parent(self, node):
        parent_id = self.parents[node]

        # Traverse Up until Parent is not equal to its Parent (Root Node - Parent of itself)
        while parent_id != self.parents[parent_id]:
            # Optimisation (Path Compression) - Move node up the Chain to Parent's Parent
            self.parents[parent_id] = self.parents[self.parents[parent_id]]
            parent_id = self.parents[parent_id]
        return parent_id

    def union(self, n1, n2):
        p1, p2 = self.find_parent(n1), self.find_parent(n2)
        if p1 == p2:
            return False  # Parents are the same -> Cycle Found

        if self.ranks[p1] > self.ranks[p2]:
            # p1 has more children - use p1 as Parent for p2
            self.parents[p2] = p1
        elif self.ranks[p1] < self.ranks[p2]:
            # p2 has more children - use p2 as Parent for p1
            self.parents[p1] = p2
        else:
            # Equal amount of children/height for 2 nodes - Arbitrary pick parent for node
            self.parents[p1] = p2
            self.ranks[p2] += 1
        return True


def min_spanning_tree(edges, n):
    min_heap = []
    for weight, n1, n2 in edges:
        heapq.heappush(min_heap, [weight, n1, n2])

    union_find = UnionFind(n)
    mst = []

    while len(mst) < n - 1:
        weight, n1, n2 = heapq.heappop(min_heap)
        if not union_find.union(n1, n2):  # nodes form a cycle!
            continue
        else:
            mst.append([n1, n2])

    return mst

# Test Data:
edges = [
    [10, 1, 2],
    [8, 1, 3],
    [4, 2, 3],
    [4, 2, 4],
    [4, 3, 4],
    [4, 3, 5],
    [2, 4, 5],
]

print(min_spanning_tree(edges, 5))
