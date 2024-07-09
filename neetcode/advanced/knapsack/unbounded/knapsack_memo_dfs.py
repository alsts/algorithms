# Memoization Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items.
def knapsack_memo_dfs(profit, weight, capacity):
    # A 2d array where N - rows(number of items), M - columns(capacity)
    N, M = len(weight), capacity
    cache = [[-1] * (M + 1) for _ in range(N)]  # -1 -> not visited
    return dfs_helper(0, profit, weight, capacity, cache)


def dfs_helper(i, profit, weight, capacity, cache):
    # Base case: Out of Bounds - All items covered
    if i == len(profit):
        return 0
    # Memoization:
    if cache[i][capacity] != -1:  # already calculated
        return cache[i][capacity]

    # Skip item i - capacity unchanged
    cache[i][capacity] = dfs_helper(i + 1, profit, weight, capacity, cache)

    # Include item i
    new_capacity = capacity - weight[i]

    if new_capacity >= 0:  # item fits
        # Sum current item profit with the recursive max (CAN BE THE SAME ITEM -> i instead of i + 1) for Remaining capacity
        max_remaining_capacity_profit = dfs_helper(i, profit, weight, new_capacity, cache)
        new_profit_item_included = profit[i] + max_remaining_capacity_profit
        # Pick the max profit:
        cache[i][capacity] = max(cache[i][capacity], new_profit_item_included)

    return cache[i][capacity]


profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]

print(knapsack_memo_dfs(profit, weight, 8))
