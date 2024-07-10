# Time: O(2^(n + m)), Space: O(n + m)
def brute_dfs(s1, s2):
    return helper(s1, s2, 0, 0)


def helper(s1, s2, i1, i2):
    if i1 == len(s1) or i2 == len(s2):
        return 0

    if s1[i1] == s2[i2]:
        return 1 + helper(s1, s2, i1 + 1, i2 + 1)
    else:
        return max(helper(s1, s2, i1 + 1, i2), helper(s1, s2, i1, i2 + 1))


print(brute_dfs("ADB23C", "ABXC"))
