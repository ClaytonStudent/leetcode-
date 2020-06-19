# 124. Binary Tree Maximum Path Sum
# source: https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/39919/8-10-lines-two-solutions

def maxPathSum(self, root):
    def maxsums(node):
        if not node:
            return [-2**31] * 2
        left = maxsums(node.left)
        right = maxsums(node.right)
        return [node.val + max(left[0], right[0], 0),
                max(left + right + [node.val + left[0] + right[0]])]
    return max(maxsums(root))

def maxPathSum_1(self, root):
    def maxend(node):
        if not node:
            return 0
        left = maxend(node.left)
        right = maxend(node.right)
        self.max = max(self.max, left + node.val + right) # 更新max值
        return max(node.val + max(left, right), 0) # 返回值还要和0进行比较
    self.max = None
    maxend(root)
    return self.max

#  we can choose not to go through the given node, so the minimum sum of all paths ending in the given node is zero. 
#  Be careful that the maxend function is not actually returning the max path sum, it updates a global variable instead. 
#  So this line: left = maxend(node.left) will give us a max path sum, it can not be less than zero, because we can just decide not to go through node.left.
#  判断我们要不要继续走到下面的子树，如果子树的最大值小于0，则不用选择这个子树