# 题目：在O(1)时间内删除链表的节点
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Soluton(object):
    def deleteNode(self,head,val):
        if head.val == val:
            return head.next
        pre,cur = head, head.next
        while cur and cur.val != val:
            pre,cur = cur,cur.next
        if cur:
            pre.next = cur.next
        return head

A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(3)
S= Soluton()
head = S.deleteNode(A,1)
print(head.val)
print(head.next.val)
print(head.next.next)