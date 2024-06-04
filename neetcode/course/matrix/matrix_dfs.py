# count paths (backtracking)
def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])

    if (min(r, c) < 0 or
            r == ROWS or c == COLS or
            (r, c) in visit or grid[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))

    count = 0
    count += dfs(grid, r + 1, c, visit)  # right
    count += dfs(grid, r - 1, c, visit)  # left
    count += dfs(grid, r, c + 1, visit)  # up
    count += dfs(grid, r, c - 1, visit)  # down

    visit.remove((r, c))
    return count


grid_matrix = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
]

print(dfs(grid_matrix, 0, 0, set()))
