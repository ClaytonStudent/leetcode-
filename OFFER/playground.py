def reorder(nums, func):
    left, right = 0 , len(nums) -1
    while left < right:
        while not isEven(left):
            left += 1
        while isEven(right):
            right -= 1
        if nums[left] < nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
    return nums


def isEven(n):
    return n & 1 == 0
