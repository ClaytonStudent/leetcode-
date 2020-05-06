# source: https://leetcode.com/problems/leaf-similar-trees/discuss/467490/Python-Iterative-and-Recursive-Solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode):
        def leaf_nodes(node, z):
            if not node:
                return
            elif not node.left and not node.right:
                z.append(node.val)
            else:
                leaf_nodes(node.left, z)
                leaf_nodes(node.right, z)

            return z
        x = []
        y = []

        one = leaf_nodes(root1, x)
        two = leaf_nodes(root2, y)

        return one == two

class Solution_1(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def DFS(node,result):
            if not node:
                return
            if node.left is None and node.right is None:
                result.append(node.val)
            else:
                DFS(node.left,result)
                DFS(node.right,result) 
            return result
        return DFS(root1,list()) == DFS(root2,list())


# iterative
class Solution_2:

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.get_leaves(root1) == self.get_leaves(root2)

    def get_leaves(self, root: TreeNode):
        result = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr: # 注意base 条件
                continue
            if not curr.left and not curr.right:
                result.append(curr.val)
            else:
                stack.append(curr.right)
                stack.append(curr.left)  # don't forget to put left last to pop it first
        return result