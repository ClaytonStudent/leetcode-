# 450. Delete Node in a BST
# source: https://zxi.mytechroad.com/blog/tree/leetcode-450-delete-node-in-a-bst/
# analysis: 分四种情况
# 1. a 不等于 key， 递归移到左右子树
# 3. a 等于 key 且 a 为叶节点，直接返回空
# 4. a 等于 key 且 a 只有一个子树，用子树替代a
# 5. a 等于 key 且 a 有两个子树，找出 a 的后继，赋值 a 为 后继的值，删掉后继

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None: 
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if root.left != None and root.right != None: # both left and right subtrees
                sucessor = root.right
                while sucessor.left:
                    sucessor = sucessor.left
                root.val = sucessor.val  # set val to sucessor.val
                root.right = self.deleteNode(root.right,sucessor.val) # delete sucessor
            else:
                if root.left == None and root.right == None:   # leaf node
                    root = None
                elif root.left == None:   # only right subtree
                    root = root.right
                elif root.right == None: # only left subtree
                    root = root.left
        return root
            
