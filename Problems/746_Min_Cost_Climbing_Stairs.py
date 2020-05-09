# source: https://leetcode.com/problems/min-cost-climbing-stairs/solution/
# analysis: 用两个指针分别代指两个步骤？最后选取最小的那个


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        a = cost[0]
        b = cost[1]
        for i in range(2,len(cost)):
            a,b = b, min(a,b) + cost[i]
        return min(a,b)


# source: https://leetcode.com/problems/min-cost-climbing-stairs/discuss/187717/Python-easy-to-understand-3-liner
# analysis: 直接从第三个起步，比较之前两步取较小的值，加在自身上。

class Solution:
    def minCostClimbingStairs(self, cost):
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1],cost[i - 2])
        return min(cost[-1], cost[-2])

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
solution = Solution()
result = solution.minCostClimbingStairs(cost)
print(result)
