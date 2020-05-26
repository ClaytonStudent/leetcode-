class Node(object):
    def __init__(self,data):
        self.val = data
        self.next = None
class Solution(object):

    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        head = Node(0)
        temp = head
        for i in range(1,n):
            temp.next = Node(i)
            temp = temp.next
        temp.next = head

        while temp.next != temp:
            for _ in range(m-1):
                head = head.next
                temp = temp.next
            head = head.next
            temp.next = head
        return temp.val


        
