# Given a linked list, determine if it has a cycle in it.
# ----------------------------------------------------------------
# Solution: https://leetcode.com/articles/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# two pointers running on a track at different speed


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if slow is None or fast is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


class Solution_1(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


class Solution_2(object):
    def hasCycle(self, head):
        nodesSeen = set() # a set is a data type that does not accept duplicates
        while head: # when head is None, you've reached end of linkedlist
            if head in nodesSeen:
                return True
            else:
                nodesSeen.add(head)
            head = head.next # move on to next node
        return False