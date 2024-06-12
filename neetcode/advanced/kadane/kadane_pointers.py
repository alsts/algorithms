# Find a non-empty subarray with the largest sum
# Kadane's Algorithm: O(n)
def kadane(arr: list[int]):
    if not arr:
        return -1

    max_sum = arr[0]
    cur_sum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(arr)):
        if cur_sum < 0:
            cur_sum = 0
            L = R

        cur_sum += arr[R]

        if cur_sum > max_sum:
            max_sum = cur_sum
            maxL, maxR = L, R

    return [maxL, maxR]


nums = [4, -1, 2, -7, 3, 4]
nums2 = [-4, -2, -7, -1]
nums3 = []
print(kadane(nums))
print(kadane(nums2))
print(kadane(nums3))
