# 162. Find Peak Element
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def search(nums,left,right):
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                return search(nums,left,mid)
            return search(nums,mid+1,right)
        return search(nums,0,len(nums)-1)




class Solution_1(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid +1 
        return left