# source: https://leetcode.com/articles/unique-paths-ii/
# Analysis: 第一个如果为1，则是障碍，返回0；如果为0，则改为1，相当于初始化。第一行和第一列，如果为障碍设为0，如果不是障碍且前一个也不是障碍设为1.往后加个判断，如果当前不是障碍则继续是上加左，如果是障碍则为0。
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            obstacleGrid[0][0] = 1
        # first column
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i-1][0] == 1 and obstacleGrid[i][0] == 0)
        for j in range(1,n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j-1] == 1 and obstacleGrid[0][j] == 0)
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]


# source: https://leetcode.com/problems/unique-paths-ii/discuss/23410/Python-different-solutions-(O(m*n)-O(n)-in-place).
# analysis: 递归的条件要想清楚，还是不太清楚啊
class Solution:
    def uniquePathsWithObstacles(self, b):
        if not b or not b[0] or b[0][0] or b[~0][~0]: return 0  # 处理边界值
        m, n = len(b), len(b[0])
        if m == 1 and n == 1: return 1
        d = {}

        def df(x, y):
            if (x, y) in d: return d[(x,y)]     # memory
            if x == m or y == n or b[x][y] == 1: return 0   # hit a obstacle
            if x == m - 1 and y == n - 1: return 1   # reach the end
            d[(x,y)] = df(x, y + 1) + df(x + 1, y)
            return d[(x, y)]

        return df(0, 1) + df(1, 0)


# source https://leetcode.com/problems/unique-paths-ii/discuss/527282/Python-DFS%2BDP-explained-solution
# Note: lru_cache(doc) helps store the returned result of every distinct method call. It functions like a dict here,
# and you can also use a dict to do the same thing.

from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        M, N = len(obstacleGrid), len(obstacleGrid[0])

        @lru_cache(maxsize=None)
        def dfs(i, j):
            if obstacleGrid[i][j]:  # hit an obstacle
                return 0
            if i == M - 1 and j == N - 1:  # reach the end
                return 1
            count = 0
            if i < M - 1:
                count += dfs(i + 1, j)  # go down
            if j < N - 1:
                count += dfs(i, j + 1)  # go right
            return count

        return dfs(0, 0)

obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

solution = Solution()
result = solution.uniquePathsWithObstacles(obstacleGrid)
print(result)