# Question
# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.
# -----------------------------------------
# Analysis
# 一共5种方法
# 1. Brute Force : 把所有的存在一个list里面，排序，然后以一个放入ListNode
# 2. priority queue
# Definition for singly-linked list.
from queue import PriorityQueue


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # brute force
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = list()
        head = root = ListNode(None)
        for l in lists:
            while l:
                result.append(l.val)
                l = l.next
        for l in sorted(result):
            head.next = ListNode(l)
            head = head.next
        return root.next

    def mergeKLists_prioirty_queue(self,lists):
        head = result = ListNode(None)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val,l))
        while not q.empty():
            val, node = q.get()
            head.next = ListNode(val)
            head = head.next
            node = node.next
            if node:
                q.put((node.val, node))
        return result.next


a = ListNode(1)
a.next = ListNode(5)

q = PriorityQueue()
q.put((a.val,a))
q.put((a.next.val,a.next))
val, node = q.get()
print(val)
