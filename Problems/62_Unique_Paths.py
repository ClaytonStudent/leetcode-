
# source: https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-62-unique-paths/
# analysis: 到达终点前两种选择，从做左面和从上面，m,n都等于1时，有一种解，不走。
def uniquePaths_without_memory(m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    result = uniquePaths_without_memory(m-1, n) + uniquePaths_without_memory(m, n-1)
    return result

# Source: https://leetcode.com/problems/unique-paths/discuss/22975/Python-easy-to-understand-solutions-(math-dp-O(m*n)-and-O(n)-space).
# Analysis: 循环递推，确定基本的0，0时等一1，从1，1开始一个个计算
# O(m*n) space
def uniquePaths(m,n):
    paths = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            paths[i][j] = paths[i-1][j] + paths[i][j-1]
    return paths[-1][-1]

# O(n) space, not easy way to understand.
def uniquePaths(m, n):
    if not m or not n:
        return 0
    cur = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            cur[j] += cur[j-1]
        print(cur)
    return cur[-1]

m = 3
n = 3
result = [[0 for _ in range(n-1)] for _ in range(m)]
result = uniquePaths_without_memory(m,n)
print(result)