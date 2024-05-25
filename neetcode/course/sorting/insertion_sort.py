
# Time Complexity: O(nx2)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = int(i)  # need a secondary variable to perform swap

        while j > 0 and arr[j - 1] > arr[j]:
            # perform swap
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


sorted_arr = insertion_sort([2, 3, 4, 1, 6])
print(sorted_arr)
