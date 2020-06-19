# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: 'TreeNode'):
        if not root: return []
        vals = []
        def preorder(root, x, y):
            if not root: return
            vals.append((x, y, root.val))
            preorder(root.left, x - 1, y + 1)
            preorder(root.right, x + 1, y + 1)
        preorder(root, 0, 0)
        ans = []
        last_x = -1000
        for x, y, val in sorted(vals):
            if x != last_x:
                ans.append([])
                last_x = x
            ans[-1].append(val)
        return ans
