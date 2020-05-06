# 257. Binary Tree Paths

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if not root:
            return []
        
        def DFS(root,result,tmp):
            if not root:
                return 
            if not root.left and not root.right:
                result.append(tmp)
            if root.left:
                DFS(root.left,result,tmp +'->' + str(root.left.val))
            if root.right:
                DFS(root.right,result,tmp +'->' + str(root.right.val))
            return result
        return DFS(root,result,str(root.val))


# dfs recursively
def binaryTreePaths(self, root):
    if not root:
        return []
    res = []
    self.dfs(root, "", res)
    return res

def dfs(self, root, ls, res):
    if not root.left and not root.right:
        res.append(ls+str(root.val))
    if root.left:
        self.dfs(root.left, ls+str(root.val)+"->", res)
    if root.right:
        self.dfs(root.right, ls+str(root.val)+"->", res)