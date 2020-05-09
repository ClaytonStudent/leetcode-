# problem: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recurive
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right,val)
        else:
            root.left = self.insertIntoBST(root.left,val)
        return root

# Iterative, 注意最后返回根节点，如果直接让根节点一步步往下走，则会丧失掉信息，所以需要curr来走。每一步判断并更新或设计新的节点并返回根节点
# source: https://leetcode.com/problems/insert-into-a-binary-search-tree/discuss/460094/Python-Iterative%3A-96-ms-92
class Solution_2(object):
    def insertIntoBST(self,root,val):
        curr = root
        while curr:
            if curr.val > val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                else:
                    curr = curr.right

