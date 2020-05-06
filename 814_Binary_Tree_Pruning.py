# source: https://leetcode.com/problems/binary-tree-pruning/solution/

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def containsOne(node):
            if not node:
                return False
            a1 = containsOne(node.left)
            a2 = containsOne(node.right)   # 查找是否包含1
            if not a1:
                node.left = None     # 如果包含则用None来替代，剪枝
            if not a2:
                node.right = None
            return node.val == 1 or a1 or a2   # 包含1的条件，父节点为1或左右子树包含1
    
        if containsOne(root):
            return root
        else:
            return None

# source: https://leetcode.com/problems/binary-tree-pruning/discuss/596746/PYTHON-3-DFS-Easy-Solution
class Solution_1:
    def pruneTree(self, root):
        def dfs(node):
            if not node:
                return
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if not node.left and not node.right and not node.val: # base case 如果一个叶节点值为0，则可以删除掉
                return None
            return node # 不要忘记return 原先的node，值得prun发生
        return dfs(root)