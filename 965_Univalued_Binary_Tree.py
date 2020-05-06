class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# source: https://leetcode.com/problems/univalued-binary-tree/discuss/469876/Python-3-(five-lines)-(beats-~93)-(Simple-Recursion)
# analysis: 设置一个唯一的root值，查看每一个子节点的值是不是匹配
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def UBT(node):
            if not node:
                return True
            if node.val != root.val:
                return False
            return UBT(node.left) and UBT(node.right)
        return UBT(root)


#source: https://leetcode.com/problems/univalued-binary-tree/discuss/440997/Accepted-Python-Answer%3A-Easy-to-Understand
# analysis: 对每个结点，如果有左右子节点，查看他们的子节点和父节点是不是同值
class Solution_1:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True        
        if (root.left and root.val != root.left.val) or (root.right and root.val != root.right.val):
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)