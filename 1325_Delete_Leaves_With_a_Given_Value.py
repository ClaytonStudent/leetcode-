#source: https://leetcode.com/problems/delete-leaves-with-a-given-value/discuss/526084/python-greater90-short-(6-lines)-and-easy-explained
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left,target) 
        root.right = self.removeLeafNodes(root.right,target) 
        if root.val == target and not root.left and not root.right:   # base case
            root = None
        return root