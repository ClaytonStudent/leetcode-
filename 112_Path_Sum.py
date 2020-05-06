# https://leetcode.com/problems/path-sum/discuss/36360/Short-Python-recursive-solution-O(n)

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    # 1:27
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True        
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

# source: https://leetcode.com/problems/path-sum/discuss/36486/Python-solutions-(DFS-recursively-DFS%2Bstack-BFS%2Bqueue)
class Solution_1:
    def hasPathSum(self, root, sum: int):
        queue = [(root, sum)]   # stack = [(root, sum)]
        while queue:
            node, value = queue.pop(0)   # node, value = stack.pop()
            if node:
                if not node.left and not node.right and node.val == value: return True
                queue.append((node.right, value - node.val))
                queue.append((node.left, value - node.val))
        return False