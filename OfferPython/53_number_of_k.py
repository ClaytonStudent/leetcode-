def firstk(nums,k,left,right):
    if left > right:
        return -1
    while left <= right:
        mid = (left+right)//2
        m_val = nums[mid]
        if m_val == k:
            if (mid > 0 and nums[mid-1]!=k) or mid==0:
                return mid
            else:
                right = mid -1
        elif m_val < k:
            left = mid + 1
        else:
            right = mid -1 

def lastk(nums,k,left,right):
    if left > right:
        return -1
    while left < right:
        mid = (left+right)//2
        m_val = nums[mid]
        if m_val == k:
            if (mid < len(nums)-1 and nums[mid+1]!=k) or mid==len(nums)-1:
                return mid
            else:
                left = mid + 1
        elif m_val < k:
            left = mid + 1 
        else:
            right = mid -1 

def numberofk(nums,k):
    if not nums:
        return 0
    left, right, number = 0, len(nums)-1, 0
    first = firstk(nums,k,left,right)
    last = lastk(nums,k,left,right)
    if first > -1 and last > -1:
        number = last - first +1
    return number

class Solution:
    def search(self, nums: [int], target: int) -> int:
        # 搜索右边界 right
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target: i = m + 1
            else: j = m - 1
        right = i
        # 若数组中无 target ，则提前返回
        if j >= 0 and nums[j] != target: return 0
        # 搜索左边界 left
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            else: j = m - 1
        left = j
        return right - left - 1

class Solution:
    def search(self, nums: [int], target: int) -> int:
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar: i = m + 1
                else: j = m - 1
            return i
        return helper(target) - helper(target - 1)



nums = [1,2,3,3,3,3,4,5]
number = numberofk(nums,3)