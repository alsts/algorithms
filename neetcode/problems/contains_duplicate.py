def contains_duplicate(nums: list[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


print(contains_duplicate([1, 2, 5, 2, 3]))
print(contains_duplicate([1, 2, 6, 9]))
