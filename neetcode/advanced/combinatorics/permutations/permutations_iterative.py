# Time: O(n^2 * n!)
def permutations_iterative(nums):
    perms = [[]]

    # Loop through Each Number:
    for n in nums:
        cur_num_perms = []
        # Loop through Previous round permutations:
        for p in perms:
            # Loop through Slots for insertion of number:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, n)
                cur_num_perms.append(p_copy)
        perms = cur_num_perms

    return perms


print(permutations_iterative([1, 2, 3, 4]))