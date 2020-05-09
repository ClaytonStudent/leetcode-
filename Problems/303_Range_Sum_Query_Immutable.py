# source: https://leetcode.com/articles/range-sum-query-immutable/
# 1. brute force
# 2. space to time: 预先计算所有的值，存储在pair里面，需要的时候调用
# 3. trade: 计算累加数组，需要的时候，后一个减去前一个就是所需要得中间的和(*重点)

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange_brute_force(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        self.result = 0
        for i in range(i,j+1):
            self.result += self.nums[i]
        return self.result

    def culsum(self):
        self.cul = [0] * (len(self.nums) +1)
        for i in range(len(self.nums)):
            self.cul[i+1] = self.cul[i] + self.nums[i]    # self.cul += [self.cul[i] + self.nums[i]] 这样可以不需要预先确定数组大小，也可以append数组

    def sumRange_caching(self,i,j):
        return self.cul[j+1] - self.cul[i]

# analysis: 先在最前面放一个零，计算累加存储下来，需要的时候用用后一个index+1减去前一个index
class NumArray_one_more(object):
    def __init__(self, nums):
        self.accu = [0]
        for num in nums:
            self.accu += self.accu[-1] + num,

    def sumRange(self, i, j):
        return self.accu[j + 1] - self.accu[i]


# analysis: my solution: one extra 0 in front of it.
class NumArray_one_more(object):
    def __init__(self, nums):
        self.accu = [0]
        for num in nums:
            self.accu += self.accu[-1] + num,
        print(self.accu)
    def sumRange(self, i, j):
        return self.accu[j+1] - self.accu[i]

nums = [-2, 0, 3, -5, 2, -1]
#numarray = NumArray(nums)
#numarray.culsum()
#result = numarray.sumRange_caching(0,5)

narray = NumArray_one_more(nums)
result = narray.sumRange(0,2)
print(result)