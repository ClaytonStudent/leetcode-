# source: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74259/Recursive-preorder-Python-and-C%2B%2B-O(n)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val)) # DFS前序遍历，其实哪种遍历都可以
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')  # 给None节点留出空间
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()
