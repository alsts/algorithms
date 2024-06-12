def longest_subarray_no_pointers(arr):
    max_length = 0

    cur_val = None
    cur_length = 1

    for item in arr:
        if cur_val == item:
            cur_length += 1
            max_length = max(cur_length, max_length)
        else:
            # previous streak ended
            cur_val = item
            cur_length = 1

    return max_length


print(longest_subarray_no_pointers([4, 2, 2, 3, 3, 3, 3, 6, 6, 6, 6, 6]))
