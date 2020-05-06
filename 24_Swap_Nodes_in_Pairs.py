# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.
# -------------------------------------------
#
# Definition for singly-linked list.
# https://www.youtube.com/watch?v=f45_eF1gmn8&list=PLH8TFsY0qnE2R9kf_9vahNY6pG9601z_4&index=16
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        dummy.next = head
        while curr.next is not None and curr.next.next is not None:
            self.swap(curr)  # swap function 可以不需要serperate，只是便于理解
            curr = curr.next.next
        return dummy.next

    def swapPairs_2(self, head): # 用self替代dummy，不用专门的方程，一行完成三个赋值，但是不容易理解
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

    def swapPairs_mine(self, head):
        curr = ListNode(None)
        curr.next = head
        root = curr

        while curr.next and curr.next.next:
            dummy = curr.next
            # 一共三步
            curr.next = dummy.next
            dummy.next = dummy.next.next
            curr.next.next = dummy
            curr = dummy # 移到下一个
        return root.next

    def swapPairs_recursive(self, head):  # recursive 解法
        if not head or not head.next:
            return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_start)
        return head
