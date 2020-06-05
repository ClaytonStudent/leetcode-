# 二叉树中和为某一值的路径，同leetcode113
def pathSum2(self, root, sum):
    if not root:
        return []
    if not root.left and not root.right and sum == root.val:   # base case 
        return [[root.val]]
    tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)  # 存储子节点的返回值
    return [[root.val]+i for i in tmp]    # 返回当前的node.val 和 他的子节点的返回（存储在tmp里面）

# 判断有没有路径，同leetcode112
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val==sum:
            return True
        sum-=root.val
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)