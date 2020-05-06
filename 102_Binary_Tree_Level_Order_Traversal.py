# source: https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)
# analysis:

# Tips: list append vs extend: https://www.geeksforgeeks.org/append-extend-python/
# append(): Adds its argument as a single element to the end of a list. The length of the list increases by one.
# extend(): Iterates over its argument and adding each element to the list and extending the list.
# The length of the list increases by number of elements in it’s argument.


#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# bfs 重点
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        ans, level = [], [root]     # ans 存储最终结果，level存储每层的node
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return ans

    # analysis: 逻辑同上，更加直观
    def levelOrder(self, root):
        ret = []
        level = [root]

        while root and level:
            currentNodes = []
            nextLevel = []
            for node in level:
                currentNodes.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            ret.append(currentNodes)
            level = nextLevel
        return ret



    # source: https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33731/Python-short-dfs-solution
    # analysis: dfs recursive.
    def levelOrder(self, root):
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if not root:
            return
        if len(res) < level + 1:  # 每到下一层，先append一个空的list
            res.append([])
        res[level].append(root.val)  # 把当前level的这个node值存储到对应的level的结果中去
        self.dfs(root.left, level + 1, res)  # 递归左子树
        self.dfs(root.right, level + 1, res)  # 递归右子树
