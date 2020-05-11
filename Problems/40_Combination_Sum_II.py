# 40. Combination Sum II
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates,target,0,[],res)
        return res
    
    def dfs(self,candidates,target,index,ls,res):
        if target < 0:
            return
        if target == 0:
            res.append(ls)
            return
        else:
            
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                self.dfs(candidates,target-candidates[i],i+1,ls+[candidates[i]],res)
    
