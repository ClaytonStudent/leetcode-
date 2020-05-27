class Solution():
    # 1. 递归
    def fibonacci(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n > 1:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
        else:
            return -1  # 其他情况

    # 2. 递归with memory
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memory = [-1 for _ in range(n+1)]
        if n == 0: return 0
        elif n == 1: return 1
        elif n > 1: 
            if memory[n] < 0:
                memory[n] = self.fib(n-1) + self.fib(n-2)
            return memory[n]
        else: return -1

    # 3. 循环
    def fibonacci_iterative(self,n):
        a, b = 0, 1
        for _ in range(n):
            a,b = b, a+b
        return a