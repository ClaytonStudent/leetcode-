# source: https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36239/Python-BFS-and-DFS-solutions.
# DFS
def minDepth1(self, root):
    if not root:
        return 0
    # 如果只有一边，则是最深的depth
    if None in [root.left, root.right]:
        return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
    else:
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


import collections
# BFS   
def minDepth(self, root):
    if not root:
        return 0
    queue = collections.deque([(root, 1)])
    while queue:
        node, level = queue.popleft()
        if node: # 对node的判断不能省略，否则有null就会进入无限循环
            if not node.left and not node.right:
                return level
            else:
                queue.append((node.left, level+1))  # 注意append的时候按照格式来
                queue.append((node.right, level+1))
