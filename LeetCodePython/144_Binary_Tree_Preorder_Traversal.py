# -------------------------------------------------------------------------------
# recurssive solutons
# 逻辑相同，都是递归地调用函数base case 是root为空地话则返回空,如果不为空，按照preorder地顺序来加入
# -------------------------------------------------------------------------------
# source: https://www.youtube.com/watch?v=COBCEDPncus
# analysis: 递归求解，preorder 中左右的顺序
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# recurssive my solution
class Solution(object):
    def __init__(self):
        self.res = []
    def preorderTraversal(self,root):
        if root:
            self.res.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.res


# recurssive soluton 1
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
        res.append(node.val)
        self.DFS(node.left,res)
        self.DFS(node.right,res)

# recurssive soluton 2
class Solution_2(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


# source: https://leetcode.com/problems/serialize-and-deserialize-bst/discuss/502589/Python-O(n)-sol-by-pre-order-traversal.-75%2B-With-explanation
# analysis: idea from other problem's solution.  Same as my soluton
class Solution_3:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """        
        # record of preorder traversal path
        path_of_preorder = []
        
        # Generate pre-order traversal path of binary search tree
        def helper( node ):
            
            if node:
                path_of_preorder.append( node.val )
                helper( node.left )
                helper( node.right )
        helper( root )
        return path_of_preorder

# -------------------------------------------------------------------------------
# iterative solutons
# -------------------------------------------------------------------------------

# source: https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/45273/Very-simple-iterative-Python-solution
# analysis: first add root, then left, then right. 第一个比较难理解，第二三逻辑相同
class Solution_11(object):
    def preorderTraversal(self,root):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)   # first前
                stack.append(node.right)  # 重点:先压入右边，再压入左边，因为是先入后出的顺序，等取出来的时候就是先左后右
                stack.append(node.left)
        return res

class Solution_12(object):
    def preorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.left   
            if not stack:          
                return res
            node = stack.pop()    
            root = node.right     


class Solution_13(object):
    def preorderTraversal(self, root):
        stack, res =[], []
        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)     # 把res提前到进入下一层之前
                root=root.left
            else:
                root=stack.pop()
                root=root.right
        return res


