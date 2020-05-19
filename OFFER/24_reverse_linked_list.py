# 题目：反转一个链表并输出它的头节点
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None


def reverse_link(head):
    if not head or not head.next:
        return head
    then = head.next
    head.next = None
    last = then.next
    while then:
        then.next = head
        head = then
        then = last
        if then:
            last = then.next
    return head

# source https://leetcode.com/problems/reverse-linked-list/submissions/
def reverse_link_(head):
    node = None
    while head:
        dummy = head.next
        head.next = node
        node,head = head,dummy
    return node
