# 90. Subsets II
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        self.dfs(nums,0,[],ans)
        return ans
    def dfs(self,nums,index,path,ans):
        ans.append(path)
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums,i+1,path+[nums[i]],ans)
        