def sum_numbers(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums.pop(0) + sum_numbers(nums)


def sum_numbers2(nums):
    if not nums:
        return 0
    else:
        return nums[0] + sum_numbers2(nums[1:])


print(sum_numbers([1, 2, 3, 7, 5, 6, 19]))
print(sum_numbers2([1, 2, 3, 7, 5, 6, 19]))
