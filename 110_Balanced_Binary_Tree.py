# source: https://leetcode.com/problems/balanced-binary-tree/discuss/362017/Python3-recursively
# analysis: base case 是左右子树的高度相差不超过1，且左右子树同样是满足
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """ 
        if root == None:
            return True
        l = self.depth(root.left)
        r = self.depth(root.right)
        return (abs(l-r) <2) and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def depth(self,node):
        if node == None: return 0
        return max(self.depth(node.left),self.depth(node.right))+1


# source: https://leetcode.com/problems/balanced-binary-tree/discuss/35708/VERY-SIMPLE-Python-solutions-(iterative-and-recursive)-both-beat-90
class Solution_1(object):
    def isBalanced(self, root): 

        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return check(root) != -1