# Time: O(n^2 * n!)
def permutations_recursive(nums):
    return helper(0, nums)


def helper(i, nums):
    if i == len(nums):  # Base Case -> Reached last number index + 1
        return [[]]

    cur_number_perms = []
    prev_number_perms = helper(i + 1, nums)
    # Loop through Previous number Permutations
    for p in prev_number_perms:
        # Insert Current Number into all slots
        for j in range(len(p) + 1):
            p_copy = p.copy()
            p_copy.insert(j, nums[i])
            cur_number_perms.append(p_copy)

    return cur_number_perms


print(permutations_recursive([1, 2, 3, 4]))
