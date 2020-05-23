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


def is_post_order(order):
    length = len(order)
    if length:
        root = order[-1]
        left = 0
        while order[left] < root:
            left += 1
        right = left
        while right < length - 1:
            if order[right] < root:
                return False
            right += 1
        left_ret = True if left == 0 else is_post_order(order[:left])
        right_ret = True if left == right else is_post_order(order[left:right])
        return left_ret and right_ret
    return False

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