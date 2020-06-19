# 题目：找出数组中的重复数字，所有数字在1-n范围内

class Solution():
    # 1. 排序，然后逐个对比，时间复杂度 O(nlogn)
    def findRepeatNumber(self,nums):
        if len(nums) <= 1:
            return -1
        nums.sort()  # sort need O(nlogn)
        for i in range(len(nums)-1):   
            if nums[i] == nums[i+1]:
                return nums[i]

    # 2. 使用字典用额外空间存储
    # 时间复杂度 O(n) , 空间复杂度 O(n)
    def findRepeatNumber(self, nums):
        dic = {}
        for n in nums:
            dic[n] = dic[n]+1 if dic.get(n) else 1
            if dic[n] > 1:
                return n
        return -1

    # 3. 交换, 利用特性，尽管双重循环，每个数字最多交换两次就能找到它的位置。
    # 时间复杂度是 O(n), 空间复杂度是O(1)
    def findRepeatNumber(self,nums):
        for i in range(len(nums)):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
        return -1

