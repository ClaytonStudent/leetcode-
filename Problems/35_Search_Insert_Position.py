# 35. Search Insert Position
# source: https://leetcode.com/problems/search-insert-position/discuss/357893/Python-Solutions-linearbisectbinary-search
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<1:
            return 0
        for i,val in enumerate(nums):
            if val>= target:
                return i
        return len(nums)

class Solution_1(object):
    def searchInsert(self,nums,target):
        lower,upper = 0, len(nums)-1
        while lower <= upper:
            mid = (lower + upper) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lower = mid + 1
            else:
                upper = mid -1
        return lower
    

    def searchInsert_1(self,nums,target):
        lower,upper = 0, len(nums)
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lower = mid + 1
            else:
                upper = mid 
        return lower

# ------------------------------------------------------------------------------
# with duplications
def searchInsert(self, nums, target): # works even if there are duplicates. 
    l , r = 0, len(nums)-1
    while l <= r:
        mid=(l+r)//2
        if nums[mid] < target:
            l = mid+1
        else:
            if nums[mid]== target and nums[mid-1]!=target:  # 相比于传统的相等即返回，多加一个条件，确保前一个值不等
                return mid
            else:
                r = mid-1
    return l
