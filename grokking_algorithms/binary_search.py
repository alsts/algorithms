
def binary_search(ls, item):
    low = 0
    high = len(ls)-1

    while low <= high:
        mid = (low + high) // 2
        guess = ls[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_ls = range(3, 1000, 2)

print(binary_search(my_ls, 240))
print(binary_search(my_ls, 20))