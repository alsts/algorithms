# shortest path from top left to bottom right
from collections import deque


def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()
    queue = deque()
    queue.append((0, 0))
    visited.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):  # Take snapshot of layer
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length  # Reached destination

            neighbors_directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # difference in row, different in column
            for dr, dc in neighbors_directions:

                # Base case: [out of bounds, already visited, blocked path]
                out_of_bounds = min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS
                if out_of_bounds or (r + dr, c + dc) in visited or grid[r + dr][c + dc] == 1:
                    continue

                # Valid Position: Node can be used for further traversal
                # Super Critical step to add to both QUEUE and VISITED -> layer traversal
                queue.append((r + dr, c + dc))
                visited.add((r + dr, c + dc))
        length += 1


grid_matrix = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
]

print(bfs(grid_matrix))
