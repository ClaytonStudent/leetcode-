# 530. Minimum Absolute Difference in BST
# source: https://leetcode.com/problems/minimum-absolute-difference-in-bst/discuss/338515/Python-recursive
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def DFS(node,lower,upper):
            if not node:
                return upper-lower
            return min(DFS(node.left,lower,node.val),DFS(node.right,node.val,upper))
        return DFS(root,float('-inf'),float('inf'))