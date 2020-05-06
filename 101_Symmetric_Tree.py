# source: https://leetcode.com/problems/symmetric-tree/discuss/535045/Py3-Sol%3A-in-just-few-lines-24ms-beats-97.63

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def isMirror(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return (node1.val==node2.val) and isMirror(node1.left,node2.right) and isMirror(node1.right,node2.left)
        return isMirror(root.left,root.right)


# https://leetcode.com/problems/symmetric-tree/discuss/311745/Easy-to-understand-Python
import collections
class Solution_1:
    def isSymmetric(self, root):
        if not root:
            return True
        stack = collections.deque([(root.left, root.right)])
        while stack:
            l, r = stack.pop()
            if l is None and r is None:
                continue
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True