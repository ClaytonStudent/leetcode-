# source: https://leetcode.com/problems/path-sum-iii/discuss/91942/Easy-Recursive-Python-7-lines-Solution

class Solution(object):
    def pathSum(self, root, s):
        return self.helper(root, s, [s])

    def helper(self, node, origin, targets):
        if not node: return 0
        hit = 0
        for t in targets:
            if t == node.val: 
                hit += 1                          # count if sum == target
        targets = [t-node.val for t in targets]+[origin]         # update the targets
        return hit+self.helper(node.left, origin, targets)+self.helper(node.right, origin, targets)

# source: https://leetcode.com/problems/path-sum-iii/discuss/249400/Python-iterative-DFS-with-a-stack
class Solution_1(object):
    def pathSum(self, root, total):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        
        stack = [(root, [root.val])]
        num = 0
        
        while stack:
            node, totals = stack.pop()
            
            num += totals.count(total)
                
            if node.left:
                stack.append((node.left, [x+node.left.val for x in totals]+[node.left.val]))
            if node.right:
                stack.append((node.right, [x+node.right.val for x in totals]+[node.right.val]))
        return num