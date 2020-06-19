# 题目：输入数组调整顺序使得奇数在偶数前面
class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] & 1 == 1:
                left += 1
                continue
            if nums[right] & 1 == 0:
                right -= 1
                continue
            nums[left], nums[right] = nums[right], nums[left]
        return nums

    def exchange(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums

