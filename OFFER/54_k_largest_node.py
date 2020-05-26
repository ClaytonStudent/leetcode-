class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def k_largest_node(node,k):
    ans = []
    def dfs(node):
        if node:
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
    dfs(node)
    if k <= len(ans)-1 and k > 0:
        return ans[-k]
    else:
        return -1

A = ListNode(5)
B = ListNode(3)
C = ListNode(7)
D = ListNode(2)
E = ListNode(4)
F = ListNode(6)
G = ListNode(8)
A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

ans = k_largest_node(A,1)
print(ans)