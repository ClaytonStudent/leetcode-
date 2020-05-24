# Question
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
# ----------------------------------------------------------------
# Solution
# https://leetcode.com/problems/majority-element/discuss/51712/Python-different-solutions-(dictionary-bit-manipulation-sorting-divide-and-conquer-brute-force-etc).
# https://leetcode.com/articles/majority-element/  官方解答
import collections
import random


def majority_element_brute_force(nums):
    for num in nums:
        count = sum(1 for elem in nums if elem == num)  # 计算每个元素出现的次数，用sum来加
        if count > len(nums) // 2:
            return num


def majority_element_hash_map(nums):
    count = collections.Counter(nums)
    return max(count.keys(), key=count.get)  # key 是一个匿名函数，对每一个count里面的key计算他的数字，最后返回数字最大的那个key


def majority_element_sorting(nums):  # Sorting: 排序后中间的那个一定是majority element
    nums.sort()
    return nums[len(nums)//2]


def majority_element_randomization(nums):   # 随机选择一个假设它是，判断计数，如果不是则继续选择
    candidate = random.choice(nums)
    while True:
        if sum(1 for num in nums if candidate == num) > len(nums) // 2:
            return candidate


def majority_element_one_pass(nums):  # one pass + dictionary
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    for num in nums:
        if dic[num] > len(nums)//2:
            return num


def majority_element_two_pass(nums):  # one pass + dictionary
    dic = {}
    for num in nums:
        count = 0
        if num not in dic:
            dic[num] = 1
        if dic[num] > len(num)//2:
            return num
        else:
            dic[num] += 1


def majority_element_divide_anc_conquer(nums):  # Divide and Conquer
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    a = majority_element(nums[:len(nums)//2])
    b = majority_element(nums[len(nums)//2:])
    print(a,b)
    if a == b:
        return a
    return [b, a][nums.count(a) > len(nums)//2]


def majority_element(nums):
    count, cand = 0, 0
    for num in nums:
        if num == cand:  # 如果相等，则计数加一
            count += 1
        elif count == 0:
            cand, count = num, 1  # 如果计数为0，则重新把下一个数赋值给cand，计数加一， 这个顺序也很重要。
        else:
            count -= 1  # 如果不相等，则计数减一
    print('count of this part',count)
    return cand
# https://leetcode.com/problems/majority-element/discuss/616413/Best-solution-for-real-interview%3A-Quick-Select!
# Partition 
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
result = majority_element_divide_anc_conquer([1,2,2,2,2,3])
print(result)