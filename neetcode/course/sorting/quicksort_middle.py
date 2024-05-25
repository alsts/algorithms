# Time Complexity: O(nlogn), worst case O(nx2)
# Reuses the same array


def partition(arr, left, right):
    i = left
    pivot = arr[right]

    for n in range(left, right):
        if arr[n] < pivot:
            arr[i], arr[n] = arr[n], arr[i]
            i += 1

    arr[right], arr[i] = arr[i], arr[right]
    return i


def quicksort(arr, left, right):
    mid = (left + right) // 2
    arr[right], arr[mid] = arr[mid], arr[right]  # pick the mid as pivot every time -> extra swap
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)


nums = [6, 2, 4, 1, 3]
quicksort(nums, 0, len(nums) - 1)
print(nums)
