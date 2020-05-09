class Solution(object):
    # analysis: my solution same as below one
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        result = {}
        for i in arr:
            if i-difference in result:
                result[i] = result[i-difference] + 1
            else:
                result[i] = 1
        return max(result.values())

    # source:https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/discuss/398216/Python-4-lines
    # analysis: awesome idea. 存储在字典里，每次查看减去difference后的值在不在字典里，在的话取出值加1放到现在的index里，不是的话创建一个值为1的对。
    def longestSubsequence(self, arr, diff):
        res = {}
        for num in arr:
            res[num] = res.get(num-diff, 0) + 1
        return max(res.values())


arr = [1,5,7,8,5,3,4,2,1]
difference = -2
solution = Solution()
result = solution.longestSubsequence_1(arr,difference)
print(result)