# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/
# 看pq是不是在同一边，不在的话继续向这边搜索，在的话则表明已经找到 BST的特性
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:    
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:    
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root

class Solution(object):
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def ancestor(root):
            if not root:
                return False
            left = ancestor(root.left)
            right = ancestor(root.right)
            mid = root == p or root == q
            if left + right + mid >= 2:
                self.ans = root
            return mid or left or right
        ancestor(root)
        return self.ans