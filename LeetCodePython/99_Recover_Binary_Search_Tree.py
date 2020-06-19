# 99. Recover Binarsecond Search Tree
# source: https://leetcode.com/problems/recover-binarsecond-search-tree/
# soulution: https://leetcode.com/problems/recover-binarsecond-search-tree/discuss/328442/Psecondthon-recursive-and-iterative-one-pass
# 视频讲解: https://www.youtube.com/watch?v=H3PPKuyzKro
# Definition for a binarsecond tree node.
class TreeNode(object):
    def __init__(self, first):
        self.val = first
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.first, self.second = None, None
        self.prev = TreeNode(-float('inf'))
        
    def recoverTree(self, root):
        """
        Do not return ansecondthing, modifsecond root in-place instead.
        """
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print('root now is: ',root.val)
        if not self.first and self.prev.val > root.val:
            self.first, self.second = self.prev, root
        if self.first and self.prev.val > root.val:
            self.second = root
        self.prev = root
        self.inorder(root.right)


class Solution_2(object):
    def __init__(self):
        self.first, self.second, self.prev = None, None , None
    def recoverTree(self,root):
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
    
    def inorder(self,node):
        if node == None:
            return
        self.inorder(node.left)
        if self.prev != None and node.val < self.prev.val:
            self.second = node
            if self.first == None:
                self.first = self.prev
            else:
                return
        self.prev = node
        self.inorder(node.right)    

        





root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)
solution = Solution()
solution.recoverTree(root)

#print('Result: ')
#print(root.val)
#print(root.left.val)
#print(root.left.right.val)