
# source: https://leetcode.com/articles/climbing-stairs/
# source: https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-70-climbing-stairs/
# 1. brute force:
# 2. Recursion with Memoization


def climbing_stairs_brute_force(i,n):
    if i > n:
        return 0
    if i == n:
        return 1
    return climbing_stairs_brute_force(i+1,n) + climbing_stairs_brute_force(i+2,n)


def climbing_stairs_with_memo(i,n,m):
    if i > n:
        return 0
    if i == n:
        return 1
    if m[i] > 0:
        return m[i]
    m[i] = climbing_stairs_with_memo(i+1,n,m) + climbing_stairs_with_memo(i+2,n,m)


def climbing_stairs_loop(nums):
    f = [1,1]
    for i in range(2,nums+1):
        f.append(climbing_stairs_loop(i-1) + climbing_stairs_loop(i-2))
    return f[nums]


def climbing_stairs_with_memory(n):  # 重点
    result = [0] * (n+1)

    def number_of_stairs(n):
        if n <= 1:
            return 1
        if result[n] > 0:      # memory: 如果此值不为0，则是已经计算过的，直接返回结果，不用再次计算。
            return result[n]
        result[n] = number_of_stairs(n - 1) + number_of_stairs(n - 2)
        return result[n]
    return number_of_stairs(n)



n = 6
print(climbing_stairs_with_memory(n))
