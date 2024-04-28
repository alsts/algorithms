def max_number(nums):
    if len(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    sub_max = max_number(nums[1:])
    return nums[0] if nums[0] > sub_max else sub_max


# print(max_number([1, 2, 3, 7, 5, 6, 19, 3, 4, 5, 3]))
print(max_number([10, 2]))
# print(max_number([3]))
