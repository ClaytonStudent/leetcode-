# Definition for singly-linked list.
from collections import deque


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []   # 把值存入到两个栈里面，以便后面pop
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        root = None # 这个是最后的一位，所以是None而不是ListNode
        carry = 0
        while stack1 or stack2 or carry:
            if stack1:
                carry += stack1.pop()
            if stack2:
                carry += stack2.pop()
            newNode = ListNode(carry%10)   # 从后往前移动node
            carry = carry // 10
            newNode.next = root   # 最后的order很重要
            root = newNode
        return root


# analysis: 先分别存储加起来，再转成str，遍历一个一个存储
class Solution_1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        num1,num2= 0, 0
        while l1:
            num1 = num1*10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2*10 + l2.val
            l2 = l2.next
        head = root = ListNode(None)
        for num in str(num1+num2):
            head.next = ListNode(int(num))
            head = head.next
        return root.next