def sum_to_s(nums,target):
    left, right = 0, len(nums)-1
    while left < right:
        if nums[left] + nums[right] == target:
            return [nums[left],nums[right]]
        elif nums[left] + nums[right] < target:
            left +=1 
        else:
            right -= 1
    return []
nums = [2,7,11,15]
target = 9
ans = sum_to_s(nums,target)
print(ans)