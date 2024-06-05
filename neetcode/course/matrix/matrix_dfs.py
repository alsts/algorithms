# count paths (brute force DFS backtracking)
def dfs(grid, r, c, visited):
    ROWS, COLS = len(grid), len(grid[0])
    out_of_bounds = min(r, c) < 0 or r == ROWS or c == COLS

    # Base Cases
    # Traversal -> [out of bounds, already visited, blocked path]:
    if out_of_bounds or (r, c) in visited or grid[r][c] == 1:
        return 0
    # Reached destination [bottom right]
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visited.add((r, c))  # add to visited -> only true for one path, would be removed on backtracking to count all available paths

    count = 0
    # Recursive calls to traverse and count all available path to Destination in 4 directions:
    count += dfs(grid, r + 1, c, visited)  # right
    count += dfs(grid, r - 1, c, visited)  # left
    count += dfs(grid, r, c + 1, visited)  # up
    count += dfs(grid, r, c - 1, visited)  # down

    visited.remove((r, c))  # After node directions recursively processed -> backtrack
    return count


grid_matrix = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
]

print(dfs(grid_matrix, 0, 0, set()))
