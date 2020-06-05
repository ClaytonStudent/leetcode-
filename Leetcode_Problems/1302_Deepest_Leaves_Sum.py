# source: https://leetcode.com/problems/deepest-leaves-sum/discuss/497210/Python-easy-understanding-solution

class Solution(object):
    def __init__(self):
        self.res = 0
        self.max_depth = 0
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recursive(node, depth):
            if not node:
                return
            if depth > self.max_depth:
                self.res = node.val
                self.max_depth = depth
            elif depth == self.max_depth:
                self.res += node.val
            recursive(node.left,depth+1)
            recursive(node.right,depth+1)
        recursive(root,1)
        return self.res