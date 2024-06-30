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
            # p1 height is higher - use p1 as Parent for p2
            self.parents[p2] = p1
        elif self.ranks[p1] < self.ranks[p2]:
            # p2 height is higher - use p2 as Parent for p1
            self.parents[p1] = p2
        else:
            # Equal height for 2 nodes - Arbitrary pick parent for node
            self.parents[p1] = p2
            self.ranks[p2] += 1
        return True


union_find = UnionFind(4)

print(union_find.union(1, 2))
print(union_find.union(2, 4))
print(union_find.union(4, 1))  # Cycle Detected
