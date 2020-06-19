# 题目：反转一个链表并输出它的头节点
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

# source https://leetcode.com/problems/reverse-linked-list/submissions/
def reverse_link_(head):
    node = None
    while head:
        dummy = head.next
        head.next = node
        node,head = head,dummy
    return node
