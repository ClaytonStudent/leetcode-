# 每次计算的时候，看前面是正负，是正数则加上去，是负数则抛弃掉，从当前开始
# Source: https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-53-maximum-subarray/
# Video: https://www.youtube.com/watch?v=2MmGzdiKR9Y


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.result = [nums[0]]
        for i in range(1,len(nums)):
            if self.result[i-1] <= 0:
                self.result.append(nums[i])
            else:
                self.result.append(self.result[-1] + nums[i])
        return self.result


# simple way:  https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way
# idea: 直接覆盖到原数组上，之前的累计如果小于0则不变，如果大于0则加上，最后取最大的那个值。
def maxSubArray(nums):
    for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
    return max(nums)


# another solution: https://leetcode.com/problems/maximum-subarray/discuss/20194/A-Python-solution
# idea: 两相对比，之前的最佳结果对比当前的值，取最大的。maxnumber 用来保存全局的最大的值
def maxSubArray(nums):
    curr = maxnumber = nums[0]
    for i in range(1,len(nums)):
        curr = max(curr,nums[i])
        maxnumber = max(maxnumber,curr)
    return maxnumber

nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
result = solution.maxSubArray(nums)
print(result)