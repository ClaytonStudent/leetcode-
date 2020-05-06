# source:https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# analysis: 两个指针，分别对应最低最高，然后一步步更新这两个值。这不是动态规划
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float('inf')
        maxPrice = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > maxPrice:
                maxPrice = price - minPrice
        return maxPrice

prices = [7,1,5,3,6,4]
solution = Solution()
result = solution.maxProfit(prices)
print(result)