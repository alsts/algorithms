# Find a non-empty subarray with the largest sum
# Brute Force: O(n^2)
def brute_force(arr: list[int]) -> int:
    if not arr:
        return -1

    max_sum = arr[0]
    for i in range(len(arr)):
        cur_sum = 0
        for j in range(i, len(arr)):
            cur_sum += arr[j]
            max_sum = max(max_sum, cur_sum)

    return max_sum


nums = [4, -1, 2, -7, 3, 4]
nums2 = [-4, -2, -7, -1]
nums3 = []
print(brute_force(nums))
print(brute_force(nums2))
print(brute_force(nums3))