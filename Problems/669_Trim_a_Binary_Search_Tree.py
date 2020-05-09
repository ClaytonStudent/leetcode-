# source: https://leetcode.com/problems/trim-a-binary-search-tree/solution/
class Solution(object):
    def trimBST(self, root, L, R):
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)

# analysis: recurssive and easy to understand (not entairly)
class Solution_1:
    def trimBST(self, root, L, R):
        if root is None:
            return None
        left = self.trimBST(root.left, L, R)
        right = self.trimBST(root.right, L, R)
        if L <= root.val <= R:
            root.left, root.right = left, right
            return root
        return left if left is not None else right
