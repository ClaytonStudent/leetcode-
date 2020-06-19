# 33. Search in Rotated Sorted Array
# source: https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14437/Python-binary-search-solution-O(logn)-48ms
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        lower , upper = 0, len(nums)-1
        while lower <= upper:
            mid = (lower+upper)//2
            if nums[mid] == target:
                return mid
            if nums[lower] <= nums[mid]:
                if nums[lower] <= target <= nums[mid]:
                    upper = mid -1
                else:
                    lower = mid +1
            else:
                if nums[mid] <= target <= nums[upper]:
                    lower = mid +1
                else:
                    upper = mid -1
        return -1