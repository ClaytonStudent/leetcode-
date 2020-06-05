class Solution():
    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k > pos+1:
                return self.findKthSmallest(nums[pos+1:], k-pos-1)
            elif k < pos+1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]
    # choose the right-most element as pivot   
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
        
        
# 使用堆来实现，有现成的nlargest函数
import heapq
class Solution_:
    def findKthSmallest(self, nums,k):
        return heapq.nsmallest(k, nums)[-1]

nums = [2,5,3,6,4]
S = Solution()
pos = S.findKthSmallest(nums,2)
print(pos)

S = Solution_()
pos = S.findKthSmallest(nums,2)
print(pos)