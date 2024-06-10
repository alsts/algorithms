def memoization(rows, cols, r, c, cache):
    # out of bounds
    if r == rows or c == cols:
        return 0

    if cache[r][c] > 0:
        return cache[r][c]

    # final destination
    if r == rows - 1 and c == cols - 1:
        return 1

    cache[r][c] = memoization(rows, cols, r + 1, c, cache) + memoization(rows, cols, r, c + 1, cache)
    return cache[r][c]


cache = [[0] * 4 for i in range(4)]
print(memoization(4, 4, 0, 0, cache))
