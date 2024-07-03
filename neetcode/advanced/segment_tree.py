class SegmentTree:

    def __init__(self, sum, L, R):
        self.sum = sum
        self.left = None
        self.right = None
        self.L = L
        self.R = R

    # O(n)
    @staticmethod
    def build(nums, L, R):
        # Base Case -> leaf - simply take value from array
        if L == R:
            return SegmentTree(nums[L], L, R)

        M = (L + R) // 2
        root = SegmentTree(0, L, R)

        # Recursive call to segment range in half until reaching leaves
        root.left = SegmentTree.build(nums, L, M)  # left range mid inclusive
        root.right = SegmentTree.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    # O(logn)
    def update(self, index, val):
        if self.L == self.R:  # Base case reached -> override value at segment index
            self.sum = val
            return

        # Recursive call to traverse down to leaf that has the index
        M = (self.L + self.R) // 2
        if index > M:
            self.right.update(index, val)
        else:
            self.left.update(index, val)

        # All parent chain segment sum would be updated (at this point either left or right child of node was updated!)
        self.sum = self.left.sum + self.right.sum

    # O(logn)
    def range_query(self, L, R):
        # Segment with pointers found -> return value
        if L == self.L and R == self.R:
            return self.sum

        M = (self.L + self.R) // 2
        if L > M:
            # Left pointer higher than mid -> go to Right Subtree
            return self.right.range_query(L, R)
        elif R <= M:
            # Right pointer lower or equal to mid -> go to Left Subtree
            return self.left.range_query(L, R)
        else:
            # Pointers spans across both sides
            return self.left.range_query(L, M) + self.right.range_query(M + 1, R)


arr = [5, 3, 7, 1, 4, 2]

segment_tree = SegmentTree.build(arr, 0, len(arr) - 1)

print(segment_tree.range_query(1, 5))

segment_tree.update(3, 4)
print(segment_tree.range_query(1, 5))
