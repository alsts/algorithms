# Brute Force Solution
# Time: O(2^c), Space: O(c)
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
        # Sum current item profit with the recursive max (CAN BE THE SAME ITEM -> i instead of i + 1) for Remaining capacity
        max_remaining_capacity_profit = dfs_helper(i, profit, weight, new_capacity)
        new_profit_item_included = profit[i] + max_remaining_capacity_profit
        # Pick the max profit:
        max_profit = max(max_profit, new_profit_item_included)

    return max_profit


profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]

# Post-Order DFS
print(knapsack_brute_dfs(profit, weight, 8))
