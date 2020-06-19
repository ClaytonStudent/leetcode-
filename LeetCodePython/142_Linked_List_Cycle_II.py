# 142. Linked List Cycle II


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# source: https://leetcode.com/problems/linked-list-cycle-ii/discuss/466846/AC-python-solution-using-set-97-fast
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = set()
        while head:
            if head in ans:
                return head
            ans.add(head)
            head = head.next
        return None

# source: https://leetcode.com/problems/linked-list-cycle-ii/discuss/44902/Sharing-my-Python-solution
class Solution_1:
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