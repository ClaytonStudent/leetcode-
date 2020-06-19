# 77. Combinations
class Solution(object):
    def combine(self, n, k):
        res = []
        self.dfs(range(1,n+1), k, 0, [], res)
        return res
    
    def dfs(self, nums, k, index, path, res):
        #if k < 0:  #backtracking
            #return 
        if k == 0:
            res.append(path)
            return # backtracking 
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res)


class Solution_1(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        nums = [i+1 for i in range(n)]
        self.dfs(nums,k,0,[],res)
        return res
    
    def dfs(self,nums,k,index,path,res):
        if k < 0:
            return
        if k == 0:
            res.append(path)
            return 
        else:
            for i in range(index,len(nums)):
                self.dfs(nums,k-1,i+1,path+[nums[i]],res)
                