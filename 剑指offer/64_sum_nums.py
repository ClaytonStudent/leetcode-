# 迭代
def sumNums(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res

# 递归
def sumNums_(n):
    if n == 1: return 1
    n += sumNums(n - 1)
    return n