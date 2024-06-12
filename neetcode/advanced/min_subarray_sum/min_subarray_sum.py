def min_subarray_sum(arr, target_sum):
    cur_sum, L = 0, 0
    min_length = float("inf")

    for R in range(len(arr)):
        cur_sum += arr[R]
        while cur_sum >= target_sum:
            min_length = min(R - L + 1, min_length)
            cur_sum -= arr[L]
            L += 1

    return 0 if min_length == float("inf") else min_length


print(min_subarray_sum([2, 3, 4, 2, 2, 3], 6))
