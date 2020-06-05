# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recurssion
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == val:
            return root
        elif val > root.val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)


# iteration
class Solution2(object):
    def searchBST(self,root,val):
        while True:
            if not root: return None
            if root.val == val: return root
            elif root.val < val:
                root = root.left
            elif root.val > val:
                root = root.right
        

 