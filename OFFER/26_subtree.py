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

