# source: https://leetcode.com/problems/two-sum/solution/

class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i,num in enumerate(nums):
            if target-num in d:  # 判断减去这个值之后有没有存在在字典里，如果有的话，返回这个index和另一个值得index
                return d[target-num], i 
            d[num]=i  # 把val 和 index 反过来存储

