def target_sum(arr, target):
    L, R = 0, len(arr) - 1

    while L < R:
        if arr[L] + arr[R] > target:
            R -= 1
        elif arr[L] + arr[R] < target:
            L += 1
        else:
            # sum found
            return [L, R]


print(target_sum([-1, 2, 3, 4, 7, 9], 7))
