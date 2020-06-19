# Question
# Reverse a singly linked list.
# ----------------------------------------------------------------
# Solution recursively
# video: https://www.youtube.com/watch?v=MRe3UsRadKw&feature=youtu.be
# 1. if current is null, return
# 2. if curr's next is null, make it as head 这是最后一个node，把它当作新list的第一个node
# 3. recursively traverse the list 这里进行递归
# 4. set curr.next.next to curr 设立新的指针
# 5. set curr.next to null  删除旧的指针


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):

    def reversed_linked_list_iterative(self, head):
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    def reversed_linked_list_recursively(self,head):
        if not head or not head.next:
            return head
        reversed_node = self.reversed_linked_list_recursively(head.next)
        head.next.next = head
        head.next = None
        return reversed_node


