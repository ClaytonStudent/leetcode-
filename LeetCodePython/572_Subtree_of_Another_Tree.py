# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# source: https://leetcode.com/problems/subtree-of-another-tree/discuss/386209/Python-98-speed-with-comments
# analysis: 前序遍历，每层前面加个#是为了防止特殊的情况如s12 t2, 把两者都存在string中，最后看t是不是在s中。

class Solution(object):
    def isSubtree(self, s, t):
        def traverse_tree(node):
            if not node: 
                return None
            return f"#{node.val} {traverse_tree(node.left)} {traverse_tree(node.right)}"
        return traverse_tree(t) in traverse_tree(s)


# source:https://leetcode.com/problems/subtree-of-another-tree/discuss/386209/Python-98-speed-with-comments
# analysis: easy to understand
class Solution_1:
    def isSubtree(self, s, t):
        if not s: 
            return False
        if self.isSameTree(s, t): 
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q