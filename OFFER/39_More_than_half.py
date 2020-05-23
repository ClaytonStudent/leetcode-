def more_than_half(nums):
    dic = {}
    for n in nums:
        dic[n] = dic.get(n,0) + 1
        if dic[n] >= len(nums)//2:
            return n
    
nums = [2,2,2,2,3]
ans = more_than_half(nums)
print(ans)