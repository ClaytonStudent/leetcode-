# source: https://www.youtube.com/watch?v=COBCEDPncus
# analysis: 递归求解，preorder 左右中的顺序
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution_1(object):
    def preorderTraversal(self, root):
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
        self.DFS(node.right,res)
        res.append(node.val)

class Solution_2:
    # @param {TreeNode} root
    # @return {integer[]}
    def __init__(self):
        self.res = []
    def postorderTraversal(self, root):
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.res.append(root.val)
        return self.res

class Solution_3:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        if not root:
            return []
        if root:
            return  self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

# source: https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45785/Share-my-two-Python-iterative-solutions-post-order-and-modified-preorder-then-reverse
# analysis: first add root, then left, then right.
class Solution_01:
    # 按照前序遍历处理，最后反转
    def postorderTraversal(self, root):
        traversal, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                # pre-order, right first
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        # reverse result
        return traversal[::-1]
    
    # 比较tricky的方法，压入node值和左右节点进栈.按照中右左的顺序，pop出来的是左右中
    def postorderTraversal(self, root: TreeNode):
        stack,res = [root],[]
        while stack:
            temp = stack.pop()
            if temp:
                if isinstance(temp, TreeNode):
                    stack.append(temp.val)
                    stack.append(temp.right)
                    stack.append(temp.left)
                else:
                    res.append(temp)
        return res