# Time: O(n * 2^n), Space: O(n)
def subsets_with_duplicates(nums):
    nums.sort()
    cur_set, subsets = [], []
    helper(0, nums, cur_set, subsets)
    return subsets


def helper(i, nums, cur_set, subsets):
    if i >= len(nums):  # Base Case -> reached final level
        # Add copy of array since it is reused across recursion stack(modified when backtracking)
        subsets.append(cur_set.copy())
        return

    # decision to include nums[i]
    cur_set.append(nums[i])
    helper(i + 1, nums, cur_set, subsets)
    cur_set.pop()  # clean up

    # decision NOT to include nums[i], skip all duplicates
    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1

    helper(i + 1, nums, cur_set, subsets)


print(subsets_with_duplicates([1, 3, 2, 2]))
