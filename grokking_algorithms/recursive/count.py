def count_numbers(nums):
    if len(nums) == 0:
        return 0
    else:
        return 1 + count_numbers(nums[1:])


print(count_numbers([1, 2, 3, 7, 5, 6, 19, 3, 4, 5, 3]))
