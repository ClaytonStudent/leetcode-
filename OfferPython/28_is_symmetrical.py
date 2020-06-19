# 题目：判断二叉树是不是对称
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# From LeetCode 101,对称的条件是两颗树，根值相等且左右对称
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def isMirror(node1,node2):
            if not node1 or not node2:
                return node1==node2
            return (node1.val==node2.val) and isMirror(node1.left,node2.right) and isMirror(node1.right,node2.left)
        return isMirror(root.left,root.right)

# 前序和对称遍历判断是否相等
class Solution_1():
    def __init__(self):
        self.pre = []
        self.symm = []
    def preorder(self,node):
        if node:
            self.pre.append(node.val)
            self.preorder(node.left)
            self.preorder(node.right)
        return self.pre
    def symmorder(self,node):
        if node:
            self.symm.append(node.val)
            self.symmorder(node.right)
            self.symmorder(node.left)
        return self.symm
    def isSymmetric(self,root):
        return self.preorder(root) == self.symmorder(root)


a = ListNode(8)
b = ListNode(6)
c = ListNode(6)
d = ListNode(5)
e = ListNode(7)
f = ListNode(7)
g = ListNode(5)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

S = Solution_1()
ans = S.isSymmetric(a)
print(ans)