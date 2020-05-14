# 39. Combination Sum
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


        def dfs(candidates,target,index,path,res):
            if target < 0:
                return
            elif target == 0:
                res.append(path)
                return
            else:
                for i in range(index,len(candidates)):
                    dfs(candidates,target-candidates[i],i,path+[candidates[i]],res)
        res = []
        candidates.sort()
        dfs(candidates,target,0,[],res)
        return res
    