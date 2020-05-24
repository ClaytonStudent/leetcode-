class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        pos = self.partition(nums,l,r)
        if pos > len(nums)-k:
            return self.findKthLargest(nums[:pos],k-(len(nums)-pos))
        elif pos < len(nums) - k:
            return self.findKthLargest(nums[pos+1:],k)
        else:
            return nums[pos]
        
    def partition(self,nums,l,r):
        low = l
        while l < r:
            if nums[l]<nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low

import heapq

nums = [2,5,3,6,4]
S = Solution()
ans = S.findKthLargest(nums,2)
print(ans)

ans = heapq.nlargest(2,nums)[-1]
print(ans)