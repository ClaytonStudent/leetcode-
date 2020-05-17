def reorder(nums, func):
    left, right = 0, len(nums) - 1
    while left < right:
        while not func(nums[left]):
            left += 1
        while func(nums[right]):
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    return nums

def is_even(num):
    return (num & 1) == 0 # 不用除以取余数，而是和1并运算，如果为0则是偶数，为1则是奇数

nums = [1,2,3,4,5]
nums = reorder(nums,is_even)
print(nums)