# Time Complexity: O(nlogn), worst case O(nx2)
# Reuses the same array

def partition(nums, left, right):
    pivot_value = nums[right]
    pivot_index = left

    # pivot_index  would always have item higher than pivot after loop completion
    for j in range(left, right):  # right exclusive
        if nums[j] < pivot_value:
            nums[pivot_index], nums[j] = nums[j], nums[pivot_index]
            pivot_index += 1

    # swap pivot with item that higher -> items lower on left side of pivot, higher on right
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    return pivot_index


def quicksort(nums, left, right):
    if left < right:
        pivot = partition(nums, left, right)
        quicksort(nums, left, pivot - 1)
        quicksort(nums, pivot + 1, right)


arr = [0, 1, 4, 6, 5]
quicksort(arr, 0, len(arr) - 1)
print(arr)
