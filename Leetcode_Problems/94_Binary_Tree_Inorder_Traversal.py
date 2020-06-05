# Definition for a binary tree node.
# source: https://www.youtube.com/watch?v=COBCEDPncus
# analysis: 递归求解，inorder 左中右的顺序
class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_0(object):
    def __init__(self):
        self.result = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.inorderTraversal(root.left)
            self.result.append(root.val)
            self.inorderTraversal(root.right)
        return self.result

class Solution_1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = list()
        if root is None:
            return res
        self.DFS(root,res)
        return res

    def DFS(self,node,res):
        if node is None:
            return None
        self.DFS(node.left,res)
        res.append(node.val)
        self.DFS(node.right,res)

class Solution_2(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


# source: https://www.youtube.com/watch?v=COBCEDPncus
# https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31381/Python-recursive-and-iterative-solutions.
# iteratively
class Solution_3(object):
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left    # 1. 向left移动直到叶结点
            if not stack:          # 如果stack为空，则代表结束了，返回res
                return res
            node = stack.pop()    # 2.把结点pop出来，加到结果的list里面
            res.append(node.val)
            root = node.right     # 3.check右边的结点，如果有的话，下一轮会继续check左边的结点


class Solution_4(object):
    def inorderTraversal(self, root):
        result, stack = list(), list()
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        
        return result