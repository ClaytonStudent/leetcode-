class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    # 1. 递归
    def __init__(self):
        self.ans = []
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if head:
            self.reversePrint(head.next)
            self.ans.append(head.val)
        return self.ans

    # 2. 用栈来循环
    def reversePrint(self,head):
        while head:
            self.ans.append(head.val)
            head = head.next
        return self.ans[::-1]

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
S = Solution()
ans = S.reversePrint(a)
print(ans)
