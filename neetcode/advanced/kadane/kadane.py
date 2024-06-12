# Find a non-empty subarray with the largest sum
# Kadane's Algorithm: O(n)
def kadane(arr: list[int]) -> int:
    if not arr:
        return -1

    max_sum = arr[0]
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum = max(cur_sum, 0)  # reset to 0 if sum range is negative
        cur_sum += arr[i]
        max_sum = max(max_sum, cur_sum)

    return max_sum


nums = [4, -1, 2, -7, 3, 4]
nums2 = [-4, -2, -7, -1]
nums3 = []
print(kadane(nums))
print(kadane(nums2))
print(kadane(nums3))
