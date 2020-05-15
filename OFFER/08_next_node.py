# -*- coding:utf-8 -*-
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         self.next = None
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right: # 1. 如果有右子树，则找到右子树的最左边的节点，即后继
            pr = pNode.right
            while pr.left:
                pr = pr.left
            return pr
        while pNode.next:   # 2. 如果没有右子树，向上遍历直到其父节点的左子树是这个节点，下一个既是该父节点。
            pp = pNode.next
            if pp.left == pNode:
                return pp
            pNode = pp




   
