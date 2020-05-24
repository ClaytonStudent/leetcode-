def maxValue(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i==0 and j==0:
                continue
            if i == 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0:
                grid[i][j] += grid[i-1][j]
            else:
                grid[i][j] += max(grid[i-1][j],grid[i][j-1])
    return grid[-1][-1]


# 优化上述代码，时间复杂度O*(mn),空间复杂度O*(1)
# 当 grid 矩阵很大时， i=0 或 j = 0 的情况仅占极少数，相当循环每轮都冗余了一次判断。
# 因此，可先初始化矩阵第一行和第一列，再开始遍历递推。

def maxValue_(grid):
    m, n = len(grid), len(grid[0])
    for j in range(1,n):
        grid[0][j] += grid[0][j-1]
    for i in range(1,m):
        grid[i][0] += grid[i-1][0]
    for i in range(1,m):
        for j in range(1,m):
            grid[i][j] += max(grid[i-1][j],grid[i][j-1])
    return grid[-1][-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
ans = maxValue_(grid)
print(ans)