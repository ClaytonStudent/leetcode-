
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Method_#1 Recursive pre-oreder traversal
# source: https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/475016/Two-python-O(-n-)-sol.-based-on-recursive-and-iterative.-With-explanation
# analysis: 与binary区别不大，都是先把root加进去，没有左右之分一个个地进行递归
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = list()
        if root is None:
            return []
        self.DFS(root, res)
        return res

    def DFS(self, node, res):
        if node:
            res.append(node.val)
            for child in node.children:
                self.DFS(child, res)


# iterative
class Solution(object):
    def preorder(self,root):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)   # first前
                for child in node.children[::-1]: # push in reverse order, and the pop in the right order.
                    stack.append(child)
        return res