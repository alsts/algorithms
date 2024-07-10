# Time: O(n * m), Space: O(min(n,m))
def dp(s1, s2):
    C, R = (len(s1), len(s2)) if len(s1) > len(s2) else (len(s2), len(s1))

    dp = [0] * (R + 1)  # extra row at the start

    for i in range(C):
        cur_row = [0] * (R + 1)

        for j in range(R):
            if s1[i] == s2[j]:  # Comparing actual letter from words
                cur_row[j + 1] = 1 + dp[j]  # Top Left Corner cell
            else:
                top_cell = dp[j + 1]  # [+1] is current, without is top cell (previous letter of s2)
                left_cell = cur_row[j]  # [+1] is current, without is left cell (previous letter of s1)
                cur_row[j + 1] = max(top_cell, left_cell)  # Check top and left cells - get max

        dp = cur_row  # override

    return dp[R]


print(dp("ADB23C", "ABXC"))
