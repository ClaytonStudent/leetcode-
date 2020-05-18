def fibonacci_recurssive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci_recurssive(n-1) + fibonacci_recurssive(n-2)
    else:
        return -1  # 其他情况


def fibonacci_iterative_with_memo(n):
    memory = {}
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n>1:
        if n not in memory:
            memory[n] = fibonacci_iterative(n-1) + fibonacci_iterative(n-2)
        return memory[n]
    else:
        return -1


def fibonacci_iterative_with_memo_2(n):
    memory = [-1 for _ in range(n+1)]
    if n == 0:
        return 0
    elif n ==1:
        return 1
    elif n > 1:
        if memory[n] < 0:
            memory[n] = fibonacci_iterative_with_memo_2(n-1) + fibonacci_iterative_with_memo_2(n-2)
        return memory[n]
    else:
        return -1


def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a,b = b, a+b
    return a

print(fibonacci_recurssive(6))
print(fibonacci_iterative_with_memo(6))
print(fibonacci_iterative(6))
print(fibonacci_iterative_with_memo_2(6))