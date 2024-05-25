def binary_search(arr: list[int], search_el: int) -> int:
    left, right = 0, len(arr)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > search_el:
            right = mid - 1
        elif arr[mid] < search_el:
            left = mid + 1
        else:
            return mid

    return -1


nums = [i for i in range(0, 100, 2)]

print(binary_search(nums, 3))
print(binary_search(nums, 8))
