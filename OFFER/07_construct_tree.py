class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        index = inorder.index(root_val)
        root = ListNode(root_val)
        root.left = self.buildTree(preorder[1:1+index],inorder[:index])
        root.right = self.buildTree(preorder[1+index:],inorder[index+1:])
        return root
preorder = [1,2,4,7,3,5,6,8]
inorder = [4,7,2,1,5,3,8,6]
S = Solution()
root = S.buildTree(preorder,inorder)

