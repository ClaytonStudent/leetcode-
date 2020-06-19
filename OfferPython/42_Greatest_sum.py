# 如果前面和小于等于0，则赋值当前值，如果前面和大于0，累加
def max_sum(nums):
    ans = float('-inf')
    current = 0
    for n in nums:
        if current <= 0:
            current = n
        else:
            current += n
        ans = max(ans,current)
    return ans

nums = [1,-2,3,10,-4,7,2,-5]
ans = max_sum(nums)
print(ans)