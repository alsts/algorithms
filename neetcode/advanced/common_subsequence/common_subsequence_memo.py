# Time: O(n * m), Space: O(n + m)
def memo_dfs(s1, s2):
    N, M = len(s1), len(s2)
    cache = [[-1] * M for _ in range(N)]
    return helper(s1, s2, 0, 0, cache)


def helper(s1, s2, i1, i2, cache):
    if i1 == len(s1) or i2 == len(s2):
        return 0
    if cache[i1][i2] != -1:
        return cache[i1][i2]

    if s1[i1] == s2[i2]:
        cache[i1][i2] = 1 + helper(s1, s2, i1 + 1, i2 + 1, cache)
    else:
        cache[i1][i2] = max(helper(s1, s2, i1 + 1, i2, cache), helper(s1, s2, i1, i2 + 1, cache))

    return cache[i1][i2]


print(memo_dfs("ADB23C", "ABXC"))
