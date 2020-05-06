# source: my solution
# analysis: recursion without memory. Take a lot time but easy to understand.

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)

# source: https://leetcode.com/problems/n-th-tribonacci-number/discuss/345236/JavaC%2B%2BPython-Straight-Forward
# analysis: Smart Soltion! Initial a,b,c with T(-2),T(-1) and T(0) ，向前推两位，改变了之前的初始值，但是加起来是对的。
class Solution_2(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b,c = 1,0,0
        for i in range(n):
            a,b,c = b,c,a+b+c
        return c


# source: https://leetcode.com/problems/n-th-tribonacci-number/discuss/350547/Solution-in-Python-3-(beats-~100)
# analysis: begins with index 0, thus the return should be a not c.
class Solution_3(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b,c = 0,1,1
        for i in range(n):
            a,b,c = b,c,a+b+c
        return a


n = 4
solution = Solution_3()
result = solution.tribonacci(n)
print(result)