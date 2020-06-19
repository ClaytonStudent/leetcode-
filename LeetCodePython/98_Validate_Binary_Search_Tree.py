# source: https://zxi.mytechroad.com/blog/tree/leetcode-98-validate-binary-search-tree/
# analysis: Recursion. 左子树小于跟，跟小于有子树。根据值得范围来递归地判断。

# inorder遍历则值是顺序地
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root)

    def helper(self,node,lower=float('-inf'),upper=float('inf')):
        if not node:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        return self.helper(node.left,lower,node.val) and self.helper(node.right,node.val,upper)


class Solution_1:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [(root,float('-inf'),float('inf')),]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right,val,upper))
            stack.append((root.left,lower,val)) 
        return True


# source: https://leetcode.com/problems/validate-binary-search-tree/solution/
# inorder: 先到最左子树，把他地值跟-inf比，更新inorder地值，然后往上走一个，比较，在走到右子树。再往上走一个。这些一开始都存在stack里面。
class Solution_2(object):
    def isValidBST(self,root):
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
