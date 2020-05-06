# 543. Diameter of Binary Tree
# source: https://leetcode.com/problems/diameter-of-binary-tree/discuss/574598/Python-simple-recursive-solution-36-ms-faster-than-96.53
# analysis: 更新diameter，最后的返回值是重点 max(left_path, right_path)+1
# because if you are to look at including the parent node, we can only take one of the children.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def path_length(self, root):
        if root:
            left_path = self.path_length(root.left)
            right_path = self.path_length(root.right)
            path = left_path + right_path
            if path > self.diameter:
                self.diameter = path    
            return max(left_path, right_path)+1
        return 0
        
    def diameterOfBinaryTree(self, root):
        self.diameter = 0   #  这里的diameter需要是global的
        self.path_length(root)
        return self.diameter




