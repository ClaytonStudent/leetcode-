# 153. Find Minimum in Rotated Sorted Array
class Soluton(object):
    def findMin(self,nums):
        if not nums:
            return None
        if nums[0] <= nums[-1]:
            return nums[0]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) //2
            if nums[mid] > nums[mid+1]:
                return mid+1
            if nums[mid-1] > nums[mid]:
                return mid
            if nums[mid] < nums[0]:
                right = mid -1
            else: 
                left = mid + 1

# source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/
# analysis: compare with the first element to decide the move direction.
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[right] > nums[0]:
            return nums[0]

        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) / 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1


# simple and easy way
# source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/396767/Simple-Binary-Search
    def findMin(self, nums):
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] > nums[hi]:
                lo = mid+1
            else:
                hi = mid
        return nums[lo]