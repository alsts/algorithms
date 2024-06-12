def close_duplicates_sliding_window(arr, k):
    window = set()
    L = 0

    for R in range(len(arr)):
        if R - L + 1 > k:  # False only when window k is not fully grown
            window.remove(arr[L])  # Shift window to the right
            L += 1
        if arr[R] in window:  # Duplicate found
            return True
        window.add(arr[R])

    return False


print(close_duplicates_sliding_window([1, 2, 3, 2, 2, 3], 3))
print(close_duplicates_sliding_window([1, 5, 4, 2, 7, 3], 3))
