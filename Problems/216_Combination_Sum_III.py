# 216. Combination Sum III
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        numbers = [i+1 for i in range(9)]
        self.dfs(numbers,n,0,[],ans,k)
        return ans
    
    def dfs(self,numbers,target,index,path,ans,k):
        if k ==0 and target == 0:
            ans.append(path)
        elif target < 0 or k < 0:
            return 
        else:
            for i in range(index,len(numbers)):
                self.dfs(numbers,target-numbers[i],i+1,path+[numbers[i]],ans,k-1)