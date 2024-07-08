# Dynamic Programming Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items.
def knapsack_dp(profit, weight, capacity):
    # A 2d array where N - rows(number of items), M - columns(capacity)
    N, M = len(weight), capacity
    dp = [[0] * (M + 1) for _ in range(N)]

    # Initialisation -> Fill the First column and row to reduce edge cases
    for item_id in range(N):
        dp[item_id][0] = 0
    for capacity_cells in range(M + 1):
        if weight[0] <= capacity_cells:
            dp[0][capacity_cells] = profit[0]

    # Loop starting from secondary item:
    for item_id in range(1, N):  # item
        for capacity_cells in range(1, M + 1):  # capacity cell (extra 1 at the beginning)
            # 2 Choices: include item or skip(use above cell if higher profit!)
            include = 0
            remaining_cells = capacity_cells - weight[item_id]

            if remaining_cells >= 0:  # item fits or even has extra remaining cells (take from above item)
                include = profit[item_id] + dp[item_id - 1][remaining_cells]  # extra column added if item just fits no remaining cells(0)

            skip = dp[item_id - 1][capacity_cells]  # value from item cell above
            dp[item_id][capacity_cells] = max(include, skip)

    return dp[N - 1][M]


profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]

print(knapsack_dp(profit, weight, 8))
