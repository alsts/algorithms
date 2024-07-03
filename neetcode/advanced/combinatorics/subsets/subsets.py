# Time: O(n * 2^n), Space: O(n)
def subsets_without_duplicates(nums):
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

    # decision NOT to include nums[i]
    helper(i + 1, nums, cur_set, subsets)


print(subsets_without_duplicates([1, 2, 3]))
