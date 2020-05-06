# Question
# You are given an integer array nums and you have to return a new counts array.
# The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# ----------------------------------------------------------------
# Solution
# 1. brute force: check every pair of numbers
# 2. Binary search tree(BST):


# 3. Binary index tree(BIT/Fenwick Tree))
# Introduce BIT: https://www.youtube.com/watch?v=CWDQJGaN1gY
# 思路: 转换成求频率和的问题。先排序，得出相对位置，然后input倒叙，得出相对的排名，每一个就是其排名n的(n-1)个元素的频率和
# 维护一个Freq表，比rank表大1，对每个元素更新他的Freq表，并计算前面的总和
# 最低有效位（英语：Least Significant Bit，lsb）是指一个二进制数字中的第0位（即最低位），权值为2^0，可以用它来检测数的奇偶性。


def solution_brute_force(nums):
    question_result = []
    for i in range(len(nums)):
        number = 0
        for j in range(i,len(nums)):
            if nums[i] > nums[j]:
                number += 1
        question_result.append(number)
    return question_result


# standard implmentation of a binary indexed tree (BIT)
class BIT():
    def __init__(self, nums):
        self.tree = [0]*(len(nums)+1)
    def sum_query(self, i):
        # remember agent... the index starts at 1
        output, i = 0, i+1
        while i > 0:
            output += self.tree[i]
            i -= i & (-i)
        return output
    def update(self, i, delta=0):
        i += 1
        while 0 < i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
            
class Solution:
    def countSmaller(self, nums):
        # chache the position of the numbers if they were unique and sorted
        tmp = {e: i for i, e in enumerate(sorted(set(nums)))}
        bit = BIT(tmp)
        # translate back these indexes into the original order
        tmp = [tmp[e] for e in nums]
        # traverse right to left
        output = []
        for i in tmp[::-1]:
			# query the BIT for the current count in the range (0, i)
            output.append(bit.sum_query(i-1))
            print(output)
			# register the ocurrence in the BIT
            bit.update(i, 1)
        return output[::-1]


nums = [7,1,3,2,9,2,1]
solution = Solution()
result = solution.countSmaller(nums)
print(result)
