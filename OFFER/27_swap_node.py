# 题目：输入二叉树，输出它的镜像
# 遍历的同时交换非叶节点的左右子节点
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = root.right, root.left
            self.mirrorTree(root.left)
            self.mirrorTree(root.right)
        return root

# preorder traversal and append values to the new list ret
# 按照中后前序遍历
def mirror_pre(root):
    ret = []
    def traversal(root):
        if root:
            ret.append(root.val)
            traversal(root.right)
            traversal(root.left)
    traversal(root)
    return ret

