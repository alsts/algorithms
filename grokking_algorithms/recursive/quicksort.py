counter = 0


def quicksort(array):
    if len(array) < 2:
        return array  # Base case: arrays with 0 or 1 element are already “sorted.”
    else:
        pivot = array[len(array) // 2]  # Recursive case
        less = [i for i in array if i < pivot]  # Partitioning -> Sub-array of all the elements less than the pivot
        greater = [i for i in array if i > pivot]  # Partitioning -> Sub-array of all the elements greater than the pivot
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([1, 8, 10, 2, 5, 9, 18, 3]))

book = dict()

book["avocado"] = 123
book["george"] = 2

print(book)