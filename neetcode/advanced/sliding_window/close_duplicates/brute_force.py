def close_duplicates_brute_force(arr, k):
    for L in range(len(arr)):
        window = min(len(arr), L + k)  # take min -> to cover full array and all windows
        for R in range(L + 1, window):
            if arr[L] == arr[R]:
                return True
    return False


print(close_duplicates_brute_force([1, 2, 3, 2, 2, 3], 3))
print(close_duplicates_brute_force([1, 5, 4, 2, 7, 3], 3))
