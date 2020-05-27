# 题目：输入两个二叉树，判断B是不是A的子结构
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isSubtree(self, s, t):
        if not s: 
            return False
        if self.isSameTree(s, t): 
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, p, q):
        if p and q:  # 两个都不为空
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q # 其中一个为空或者都为空

A = ListNode(4)
B = ListNode(2)
C = ListNode(3)
D = ListNode(4)
E = ListNode(5)
F = ListNode(6)
G = ListNode(7)
H = ListNode(8)
I = ListNode(9)

AA = ListNode(4)
BB = ListNode(8)
CC = ListNode(9)
AA.left = BB
AA.right = CC

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G
D.left = H
D.right = I

S = Solution()
ans = S.isSubtree(A,AA)
print(ans)