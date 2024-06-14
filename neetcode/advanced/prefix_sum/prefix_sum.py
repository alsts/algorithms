class PrefixSum:

    def __init__(self, nums: list[int]):
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)

    def range_sum(self, L, R):
        prefix_right = self.prefix[R]
        prefix_left = self.prefix[L - 1] if L > 0 else 0
        return prefix_right - prefix_left


prefix_sum = PrefixSum([2, -1, 3, -3, 4])
print(prefix_sum.range_sum(0, 3))
print(prefix_sum.range_sum(2, 3))
