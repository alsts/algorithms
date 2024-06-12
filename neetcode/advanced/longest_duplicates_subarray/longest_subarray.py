def longest_subarray(arr):
    max_length = 0
    L = 0

    for R in range(len(arr)):
        if arr[L] == arr[R]:
            window_length = R - L + 1
            max_length = max(window_length, max_length)
        else:
            # previous streak ended, reset left pointer (window)
            L = R

    return max_length


print(longest_subarray([4, 2, 2, 2, 2, 3, 3, 3]))
