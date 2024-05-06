# Time Complexity: O(nlogn), worst case O(nx2)
# Reuses the same array

def bad_quicksort(arr, s, e):
    if (e - s) + 1 <= 1:
        return arr

    pivot = arr[e]
    left = s

    # partition all elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # swap [left] with last item [pivot]
    arr[e] = arr[left]
    arr[left] = pivot

    bad_quicksort(arr, s, left - 1)
    bad_quicksort(arr, left + 1, e)

    return arr


print(bad_quicksort([6, 2, 4, 1, 3], 0, 4))
