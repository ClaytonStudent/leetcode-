# dynamic programming
# 如果面值只有1，5，11， 求取得15块钱最少用多少张纸币

def money(n):
    ans = [0] * n
    ans[0] = 0
    for i in range(1,n):
        cost = float('inf')
        if i-1 >= 0:
            cost = min(cost,ans[i-1]+1)
        if i -5 >= 0:
            cost = min(cost,ans[i-5]+1)
        if i-11 >=0:
            cost = min(cost,ans[i-11]+1)
        ans[i] = cost 
        print(i,ans[i])

# money(15)

# 最长上升子序列

def LIS(nums):
    dp = [1]* len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and dp[i]< dp[j]+1:
                dp[i] = dp[j]+1
                #print(i,dp[i])
    #maximum = 0
    #for i in range(len(dp)):
    #    maximum = max(maximum,dp[i])
    return dp

nums = [10, 22, 9, 33, 21, 50, 41, 60]
dp = LIS(nums)
print(dp)