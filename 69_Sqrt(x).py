# 69. Sqrt(x)
# source: https://leetcode.com/problems/sqrtx/discuss/25061/Python-binary-search-solution-(O(lgn)).
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left <= right:
            mid = left + (right-left)//2
            if mid*mid <= x < (mid+1) * (mid+1):
                return mid
            elif mid*mid > x:
                right = mid
            else:
                left = mid + 1
        