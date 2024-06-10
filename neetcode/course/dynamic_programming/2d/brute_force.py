def brute_force(rows, cols, r, c):
    # out of bounds
    if r == rows or c == cols:
        return 0

    # final destination
    if r == rows - 1 and c == cols - 1:
        return 1

    return brute_force(rows, cols, r + 1, c) + brute_force(rows, cols, r, c + 1)


print(brute_force(4, 4, 0, 0))
