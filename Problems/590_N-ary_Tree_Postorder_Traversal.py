
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
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
            for child in node.children:
                self.DFS(child, res)
            res.append(node.val)

# iterative
class Solution(object):
    def postorder(self,root):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                for child in node.children:
                    stack.append(child)
                res.append(node.val)
        return res[::-1]