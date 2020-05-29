# 题目：输入数组，判断是不是后序遍历序列
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# 遍历postorder树
def post(root):
    ans = []
    def dfs(root):
        if root:
            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)
    dfs(root)
    return ans


# 构建postorder 树
def postorder(nums):
    if not nums:
        return True
    root = nums[-1]
    left = [i for i in nums if i < root]
    right = [i for i in nums if i > root]
    rootNode = ListNode(root)
    rootNode.left = postorder(left)
    rootNode.right = postorder(right)
    return rootNode

class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        def recur(i,j):
            if i >= j:
                return True
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            return (p==j) and recur(i,m-1) and recur(m,j-1)
        return recur(0,len(postorder)-1)

a = ListNode(8)
b = ListNode(6)
c = ListNode(10)
d = ListNode(5)
e = ListNode(7)
f = ListNode(9)
g = ListNode(11)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

#ans = postorder(a)
#print(ans)
nums = [5, 7, 6, 9, 11, 10, 8]
head = postorder(nums)
print(head.val)
print(head.left.val)
print(head.right.val)