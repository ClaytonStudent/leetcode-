# source:
# analysis: similar to 102
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# source https://leetcode.com/problems/binary-tree-level-order-traversal-ii/discuss/35136/Simple-iterative-Python-O(n)-solution
class Solution(object):
    def levelOrderBottom(self, root):
        if not root: return []
        queue, nodes = [root], []
        while queue:
            nodes.append([q.val for q in queue])
            queue = [q for node in queue for q in (node.left, node.right) if q]
        nodes.reverse()
        return nodes

# another solution: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/discuss/34978/Python-solutions-(dfs-recursively-dfs%2Bstack-bfs%2Bqueue).
# need dig into it.