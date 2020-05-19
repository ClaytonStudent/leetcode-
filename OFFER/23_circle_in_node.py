# 题目：如果一个链表包含环，找出环的入口节点
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

# 确定有没有环,返回True False
def cycle(node):
    if not node or not node.next:
        return False
    slow = node
    fast = node.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

# 返回环的位置
# source https://leetcode.com/problems/linked-list-cycle-ii/discuss/258948/%2B-python
class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        try: ##如果有尾部，必然出错，进入except。
            Slow = head.next ## 保证Slow和 Fast同时移动
            Fast = head.next.next
            while Slow!=Fast: ## Fast一直是Slow的两倍速度，这点很关键。
                Slow = Slow.next
                Fast = Fast.next.next
        except:
            return None       
        Slow = head ##让Slow从头开始，Fast保持上一步的位置
        while Slow != Fast:
            Slow = Slow.next
            Fast = Fast.next
        return Slow

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = c
print(Solution().detectCycle(a))