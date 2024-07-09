# Dynamic Programming Solution
# Time: O(n * m), Space: O(m)
# Where n is the number of items.
def knapsack_dp(profit, weight, capacity):
    # A 2d array where N - rows(number of items), M - columns(capacity)
    N, M = len(weight), capacity
    dp = [0] * (M + 1)  # 0th the row

    # Only need 2 rows for Solution Space:
    for item_id in range(N):
        cur_row = [0] * (M + 1)

        for capacity_cells in range(1, M + 1):
            include = 0
            skip = dp[capacity_cells]  # Row above!!!

            remaining_cells = capacity_cells - weight[item_id]
            if remaining_cells >= 0:  # Item fits or even has remaining cells
                include = profit[item_id] + cur_row[remaining_cells]  # Same row referenced (Item can be reused!!!)

            cur_row[capacity_cells] = max(include, skip)  # Pick this row max or reference cell on last row!

        dp = cur_row  # Override Dp with Current Row

    return dp[M]  # Pick last item in result row - Answer


profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]

print(knapsack_dp(profit, weight, 8))
