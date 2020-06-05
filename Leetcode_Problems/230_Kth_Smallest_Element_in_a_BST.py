# Definition for a binary tree node.
# source: https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63829/Python-Easy-Iterative-and-Recursive-Solution
# analysis: iterative way.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k = k-1
            if k == 0:
                return root.val
            root = root.right


# analysis: Recursive.
class Solution_1(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)  # why this is in the middle? inorder traversal
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)