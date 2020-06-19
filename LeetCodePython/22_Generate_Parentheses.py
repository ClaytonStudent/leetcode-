# 22. Generate Parentheses
# source: https://leetcode.com/problems/generate-parentheses/solution/
# analysis: start an opening bracket if we still have one (of n) left to place. 
# And we can start a closing bracket if it would not exceed the number of opening brackets.
class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans