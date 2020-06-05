class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Serialize():
    def __init__(self):
        self.ans = ''
    def serialized(self, root):
        if root:
            self.ans += str(root.val) 
            self.serialized(root.left)
            self.serialized(root.right)
        else:
            self.ans += '$'
        return self.ans

class Codec:
    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = ListNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()
    
A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
A.left = B
A.right = C
S = Serialize()
ans = S.serialized(A)