class Solution:
    def twoSum(self, n):
        def diceCnt(n):
            if n == 1:
                return [0] + [1] * 6
            cnts = diceCnt(n - 1) + [0] * 6
            for i in range(6 * n, 0, -1):
                cnts[i] = sum(cnts[max(i - 6, 0): i])
            return cnts
        return filter(lambda a: a != 0, list(map(lambda a: a / 6 ** n, diceCnt(n))))


#####动态规划
class Solution_:
    def twoSum(self, n):
        dp = [ [0 for _ in range(6*n+1)] for _ in range(n+1)]
        for i in range(1,7):
            dp[1][i] = 1

        for i in range(2,n+1):
            for j in range(i,i*6+1):
                for k in range(1,7):
                    if j >= k+1:
                        dp[i][j] +=dp[i-1][j-k]
        res = []
        for i in range(n,n*6+1):
            res.append(dp[n][i]*1.0/6**n)
        return res


