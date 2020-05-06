# 508. Most Frequent Subtree Sum
# source: https://leetcode.com/problems/most-frequent-subtree-sum/discuss/391254/Fast-Python-Recursive-solution
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 48 ms, 99%
    def findFrequentTreeSum(self, root):
        if not root: return []
        
        D = collections.defaultdict(int)
        # DFS recursively
        def helper(node):
            if not node: return 0
            rv = node.val + helper(node.left) + helper(node.right)
            D[rv] += 1
            return rv
        
        helper(root)
        mx = max(D.values())
        return [k for k, v in D.items() if v == mx] # return key if its val == max

# source: https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
class Solution:
    def maxPathSum(self, root):
		max_path = float("-inf") # placeholder to be updated
		def get_max_gain(node):
			nonlocal max_path # This tells that max_path is not a local variable
			if node is None:
				return 0
				
			gain_on_left = max(get_max_gain(node.left), 0)  # Read the part important observations
    		gain_on_right = max(get_max_gain(node.right), 0)  # Read the part important observations
		    current_max_path = node.val + gain_on_left + gain_on_right # Read first three images of going down the recursion stack
    		max_path = max(max_path, current_max_path) # Read first three images of going down the recursion stack
		    return node.val + max(gain_on_left, gain_on_right) # Read the last image of going down the recursion stack		
	    get_max_gain(root) # Starts the recursion chain
	    return max_path		