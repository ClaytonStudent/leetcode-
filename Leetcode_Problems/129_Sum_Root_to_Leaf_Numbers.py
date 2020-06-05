# 129. Sum Root to Leaf Numbers
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# my solution
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def DFS(root,total):
            if not root:
                return 0
            if not root.left and not root.right:
                return total + root.val
            return DFS(root.left,(total+root.val)*10) + DFS(root.right,(total+root.val)*10)   
        return DFS(root,0) 


# source: https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/41468/Clean-python-Solution
# anlysis: cleaner, same logic
def sumNumbers(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def helper(sum, root):
        if not root:
            return 0   
        sum = sum * 10 + root.val
        if not root.left and not root.right:
            return sum
        return helper(sum, root.left) + helper(sum, root.right)
     
    return helper(0, root)