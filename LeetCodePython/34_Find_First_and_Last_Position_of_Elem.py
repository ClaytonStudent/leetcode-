# 34. Find First and Last Position of Element in Sorted Array
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]


class Solution_1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        low, high = 0, len(nums)-1
        first = self.findFirstIndex(nums, low, high, target)

        second = self.findLastIndex(nums, low, high, target)
        
        return [first, second]
    def findFirstIndex(self, nums, low, high, target):
        res = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                res = mid
                high = mid-1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid + 1
        return res
    
    def findLastIndex(self, nums, low, high, target):
        res = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                res = mid
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid + 1
        return res