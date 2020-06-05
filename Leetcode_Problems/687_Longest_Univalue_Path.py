# 687. Longest Univalue Path
def longestUnivaluePath(self, root):
    def dfs(root):
        """Return longest overall and longest ending at root."""
        if not root:
            return 0, 0
        l1, l2 = dfs(root.left)
        r1, r2 = dfs(root.right)        
        l2 = 1 + l2 if root.left and root.left.val == root.val else 0
        r2 = 1 + r2 if root.right and root.right.val == root.val else 0
        return max(l1, r1, l2 + r2), max(l2, r2)
    return dfs(root)[0]




class Solution(object):
    def __init__(self):
        self.ans = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def DFS(node):
            if not node:
                return 0
            left = DFS(node.left)
            right = DFS(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left + 1
            if node.right and node.right.val == node.val:
                right_arrow = right + 1
            self.ans = max(self.ans,left_arrow+right_arrow)
            return max(left_arrow,right_arrow)
        DFS(root)
        return self.ans