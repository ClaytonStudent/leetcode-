# 题目：输入二叉树，输出它的镜像
# 遍历的同时交换非叶节点的左右子节点
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def swap(root):
    if not root:
        return None
    if not root.left and not root.right:
        return None
    root.left, root.right = root.right, root.left # 交换非叶节点
    if root.left:
        swap(root.left)
    if root.right:
        swap(root.right)

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


def preorder(root):
    ret = []

    def traversal(root):
        if root:
            ret.append(root.val)
            traversal(root.left)
            traversal(root.right)
    traversal(root)
    return ret

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


ret = preorder(a)
print(ret)