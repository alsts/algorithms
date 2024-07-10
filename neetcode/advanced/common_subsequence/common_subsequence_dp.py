# Time: O(n * m), Space: O(n + m)
def dp(s1, s2):
    s1_row, s2_col = len(s1), len(s2)

    # Solution space is bigger and offset by 1 to cover Edge Cases
    dp = [[0] * (s2_col + 1) for _ in range(s1_row + 1)]  # M would represent rows, N - columns

    for s1_r in range(s1_row):
        for s2_c in range(s2_col):
            if s1[s1_r] == s2[s2_c]:  # Comparing actual letter from words
                dp[s1_r + 1][s2_c + 1] = 1 + dp[s1_r][s2_c]  # Solution space is offset by 1 compared to word-letter indexes
            else:
                top_cell = dp[s1_r + 1][s2_c]  # [+1] is current, without is top cell (previous letter of s2)
                left_cell = dp[s1_r][s2_c + 1]  # [+1] is current, without is left cell (previous letter of s1)
                dp [s1_r + 1][s2_c + 1] = max(top_cell, left_cell)  # Check top and left cells - get max

    return dp[s1_row][s2_col]


print(dp("ADB23C", "ABXC"))
