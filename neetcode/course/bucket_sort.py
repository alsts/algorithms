def bucket_sort(arr: list[int]) -> list[int]:
    number_counts = [0 for _ in range(len(arr))]
    for i in range(len(arr)):
        number_counts[arr[i]] += 1

    i = 0
    for number in range(len(number_counts)):
        for _ in range(number_counts[number]):
            arr[i] = number
            i += 1

    return arr


print(bucket_sort([2, 1, 2, 0, 0, 2]))
