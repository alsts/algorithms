# Brute Force Solution
# Time: O(2^n), Space: O(n)
# Where n is the number of items.
def knapsack_brute_dfs(profit, weight, capacity):
    return dfs_helper(0, profit, weight, capacity)


def dfs_helper(i, profit, weight, capacity):
    # Base case: Out of Bounds - all items covered
    if i == len(profit):
        return 0

    # Skip item i - capacity unchanged
    max_profit = dfs_helper(i + 1, profit, weight, capacity)

    # Include item i
    new_capacity = capacity - weight[i]

    if new_capacity >= 0:  # item fits
        # Sum current item profit with the recursive max for Remaining capacity
        max_remaining_capacity_profit = dfs_helper(i + 1, profit, weight, new_capacity)
        new_profit_item_included = profit[i] + max_remaining_capacity_profit
        # Pick the max profit:
        max_profit = max(max_profit, new_profit_item_included)

    return max_profit


profit = [4, 4, 7, 1]  # when going back in recursive stack only pick the max out of two recursive branches
weight = [5, 2, 3, 1]  # traverse through weight until reaching base case

# The order of items by weights will be preserved across all recursive branches

# 5      + 2      + [skip] + 1
# [skip] + 2      + [skip] + 1
# [skip] + [skip] + [skip] + 1
# 5      + 2      + 3 [not included in max_profit] -> reached capacity limit -> would return max as [5 + 2] only!!!!

# Post-Order DFS
print(knapsack_brute_dfs(profit, weight, 8))
