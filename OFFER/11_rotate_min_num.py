def rotate(nums):
    if len(nums) == 0:
        return False
    elif len(nums) == 1:
        return nums[0]
    left, right = 0, len(nums)-1
    mid = 0
    while nums[left] >= nums[right]:
        if right - left == 1:
            return nums[right]
        mid = (left+right)//2
        if nums[mid] >= nums[left]:
            left = mid
        elif nums[mid] <= nums[right]:
            right = mid
    return nums[mid]


def findMin(nums):
    if len(nums) == 0:
        return False
    elif len(nums) == 1:
        return nums[0]
    left,right = 0, len(nums)-1
    while left < right:
        mid = (left+right) // 2
        if nums[mid] > nums[right]:
            left = mid +1
        else:
            right = mid
    return nums[left]

nums = [3,4,5,1,2]
print(rotate(nums))
print(findMin(nums))