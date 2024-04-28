def two_sum(nums: list[int], target: int) -> list[int]:
    prev_map = {}  # val -> index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i


print(two_sum([3, 2, 4], 6))
print(two_sum([12, 5, 8, 9], 17))
