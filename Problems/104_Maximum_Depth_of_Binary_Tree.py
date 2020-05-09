# 104.Python iterative DFS and recursion
# source: https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/325012/104.Python-iterative-DFS-and-recursion

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    

class Solution_1(object):
    def maxDepth(self, root):
        ans = 0
        if not root:
            return 0
        DFS = [(root,1)] # stack
        while DFS:
            root, depth = DFS.pop()
            if depth > ans:
                ans = depth
            if root.left:
                DFS.append((root.left, depth + 1))
            if root.right:
                DFS.append((root.right, depth + 1))
        return ans

    def iterative(self, root):
        if not root:
            return 0
        stack = [[root, 1]]
        ans = 0
        while len(stack):
            root, depth = stack.pop()
            if root.left: stack.append([root.left, depth + 1])
            if root.right: stack.append([root.right, depth + 1])
            ans = max(depth, ans)
        return ans