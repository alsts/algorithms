# Given n numbers (1 - n), return all possible combinations of size k. (n choose k math problem)
# Time: (k * 2^n)
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

    # decision to include i
    cur_comb.append(i)
    helper(i + 1, cur_comb, combs, n, k)
    cur_comb.pop()

    # decision to NOT include i
    helper(i + 1, cur_comb, combs, n, k)


print(combinations(5, 2))
