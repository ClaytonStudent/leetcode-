# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# source: https://leetcode.com/problems/find-mode-in-binary-search-tree/discuss/98150/Python-easy-understand-solution
# analysis: 使用栈，时间和空间复杂度都是O(n),中序遍历，结果存储在一个dic里面，然后遍历取max val得到结果
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack=[root]
        dic={}
        result=[]
        while stack:
            node=stack.pop()
            dic[node.val]=dic.get(node.val,0)+1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        max_val=max(dic.values())        
        for key in dic.keys():
            if dic[key]==max_val:
                result.append(key)
        return result


# recurrsion: https://www.youtube.com/watch?v=v4F4x_uwMb8
# analysis: 时间和空间复杂度都是O(n),与第一个解法类似
class Solution_2(object):
    def findMode(self, root):
        if not root:
            return []
        hash = {}
        result = []

        def find_hash(root,hash):
            if not root:
                return 
            hash[root.val] = hash.get(root.val,0) + 1
            # recurssion
            find_hash(root.left,hash)
            find_hash(root.right,hash)
        find_hash(root,hash)
        max_val=max(hash.values())        
        for key in hash.keys():
            if hash[key]==max_val:
                result.append(key)
        return result

# source: https://leetcode.com/problems/find-mode-in-binary-search-tree/discuss/406028/Python-inorder-traversal-O(1)-space-with-explanation
# analzsis：空间复杂度为O(1)
class Solution_1(object):

    prev = None
    max_count = 0
    current_count = 0 
    result = []

    def findMode(self, root):
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node: return
        self.dfs(node.left)
        if node.val != self.prev.val:
            self.current_count = 1
        else:
            self.current_count + 1
        if self.current_count == self.max_count:
            self.result.append(node.val)
        elif self.current_count > self.max_count:
            self.result = [node.val]
            self.max_count = self.current_count
        self.prev = node.val
        self.dfs(node.right)


