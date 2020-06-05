# Question
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# ----------------------------------------------------------------
# Solution
# https://leetcode.com/articles/add-two-numbers/
# List + 高精度加法
# 低位在前，高位在后， 假设不会有前置得0，即最后一位不是0(除非本身这个数就是0).
# 没有提到数据规模，要考虑 时间复杂度 边界条件


class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def addTwoNumbers_solution_1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = root = ListNode(None)
        carry = 0
        p, q = l1, l2
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            val_sum = x + y + carry
            carry = val_sum // 10
            head.next = ListNode(val_sum % 10)
            head = head.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry == 1:
            head.next = ListNode(1)
        return root.next

    def addTwoNumbers_solution_2(self, l1, l2):  # 把carry放到while的loop里，对于多出来的carry也可以处理
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

    def addTwoNumbers_solution_3(self, l1, l2):  # 如果为空不用赋值为0，也不用专门设置变量存储总值，放到carry里，取模即可
        carry = 0
        root = head = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            head.next = ListNode(carry % 10)
            head = head.next
            carry = carry // 10
        return root.next

# NOTE: 初始化的时候赋值为0 ListNode(0)， 每次取完值记得更新l1和l2，

    def addTwoNumbers_solution_mine(self,l1,l2):
        carry = 0
        root = head = ListNode(None)
        while l1 or l2 or carry:
            p = q = 0
            if l1:
                p = l1.val
                l1 = l1.next
            if l2:
                q = l2.val
                l2 = l2.next
            node_sum = p + q + carry
            head.val = node_sum % 10
            carry = carry // 10
            head = head.next
        return root.next







l1 = ListNode(7)
l1.next = ListNode(9)
l1.next.next = ListNode(7)

ans = set()
while l1:
    set.add(l1)
    l1 = l1.next
print(ans)