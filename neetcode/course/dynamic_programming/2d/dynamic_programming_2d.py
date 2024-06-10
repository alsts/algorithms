def dp_bottom_up(rows, cols):
    prev_row = [0] * cols

    # traverse through cells bottom up:
    for r in range(rows - 1, -1, -1):  # from, to, step
        cur_row = ([0] * (cols - 1)) + [1]  # last item is always 1

        # calculate row cells -> move right to left, ignore rightmost item as it is always 1
        for c in range(cols - 2, -1, -1):
            cur_row[c] = cur_row[c + 1] + prev_row[c]  # sum values from right and bottom cells
        prev_row = cur_row
    return prev_row[0]


# Initial state:
# 0, 0, 0, 1
# 0, 0, 0, 0 -> prev row initial value

# Ignore last column -> all 1s
# For each cell sum previous row bottom + curr row right

print(dp_bottom_up(4, 4))
