# source: https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)
def pathSum(self, root, sum):
    if not root:
        return []
    res = []
    self.dfs(root, sum, [], res)
    return res
    
    # 逐层往下，不断地扩充ls的值，最后满足条件的话，把它存储在res里面作为结果
def dfs(self, root, sum, ls, res):
    if not root.left and not root.right and sum == root.val:
        ls.append(root.val)
        res.append(ls)
    if root.left:
        self.dfs(root.left, sum-root.val, ls+[root.val], res)
    if root.right:
        self.dfs(root.right, sum-root.val, ls+[root.val], res)
        
def pathSum2(self, root, sum):
    if not root:
        return []
    if not root.left and not root.right and sum == root.val:   # base case 
        return [[root.val]]
    tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)  # 存储子节点的返回值
    return [[root.val]+i for i in tmp]    # 返回当前的node.val 和 他的子节点的返回（存储在tmp里面）