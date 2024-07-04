# Time: (k * C(n, k))
def combinations(n, k):
    combs = []
    helper(1, [], combs, n, k)
    return combs


def helper(i, cur_comb, combs, n, k):
    if len(cur_comb) == k:
        combs.append(cur_comb.copy())
        return
    if i > n:
        return

    # multiple branches for each number
    for j in range(i, n + 1):
        cur_comb.append(j)
        helper(j + 1, cur_comb, combs, n, k)
        cur_comb.pop()  # backtrack after this to check next combination


print(combinations(5, 2))
