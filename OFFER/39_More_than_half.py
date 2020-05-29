def more_than_half(nums):
    dic = {}
    for n in nums:
        dic[n] = dic.get(n,0) + 1
        if dic[n] >= len(nums)//2:
            return n


# https://leetcode.com/problems/majority-element/discuss/616413/Best-solution-for-real-interview%3A-Quick-Select!

class Solution:
    def majorityElement(self, a):
        n = len(a)

        def partition(lo, hi):
            piv, k = a[hi], lo

            for i in range(lo, hi):
                if a[i] < piv:
                    a[i], a[k] = a[k], a[i]
                    k += 1

            a[k], a[hi] = a[hi], a[k]

            return k

        lo, hi = 0, n - 1
        mid = n // 2
        
        while True:
            k = partition(lo, hi)

            if k == mid:
                return a[mid]
            elif k < mid:
                lo = k + 1
            else:
                hi = k - 1

# 摩尔投票法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x


nums = [2,2,2,2,3]
ans = more_than_half(nums)
print(ans)