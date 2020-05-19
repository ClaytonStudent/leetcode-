# 题目：输入两个递增的链表，合并他们且仍然是递增排序
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

def merge(h1,h2):
    root = node = ListNode(None)
    while h1 and h2:
        if h1.val <= h2.val:
            node.next = h1
            h1 = h1.next
        else:
            node.next = h2
            h2 = h2.next
        node = node.next
    node.next = h1 or h2
    return root.next

# recurssive
def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        start = None    
        if l1.val < l2.val:
            start = l1
            start.next = self.mergeTwoLists(l1.next, l2)
        else:
            start = l2
            start.next = self.mergeTwoLists(l1, l2.next)
        return start