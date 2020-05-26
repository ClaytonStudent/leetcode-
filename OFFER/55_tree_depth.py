class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def depth(node):
    if not node:
        return 0
    return 1 + max(depth(node.left),depth(node.right))

A = ListNode(5)
B = ListNode(3)
C = ListNode(7)
D = ListNode(2)
E = ListNode(4)
A.left = B
A.right = C
B.left = D
B.right = E
ans = depth(A)
print(ans)

# 拓展，判断是不是平衡二叉树
# 后序遍历 + 剪枝 （从底至顶）
class Solution:
    def isBalanced(self, root):
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1
