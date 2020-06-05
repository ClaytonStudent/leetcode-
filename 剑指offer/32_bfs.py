# 题目：不分行从上到下打印二叉树
from collections import deque
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def bfs(root):    
    ans = deque()
    res = []
    if not root:
        return None
    ans.append(root)
    while ans:
        node = ans.popleft()
        res.append(node.val)
        if node.left:
            ans.append(node.left)
        if node.right:
            ans.append(node.right)
    return res

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

res = bfs(a)
print(res)