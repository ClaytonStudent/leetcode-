class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = [None for _ in A]
        l,r = 0, len(A) - 1
        for i in range(len(A)-1,-1,-1):
            if abs(A[l])>abs(A[r]):
                ans[i] = A[l]**2
                l += 1
            else:
                ans[i] = A[r]**2
                r -= 1
        return ans