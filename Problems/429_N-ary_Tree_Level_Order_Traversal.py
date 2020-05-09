# source: https://leetcode.com/problems/n-ary-tree-level-order-traversal/discuss/506649/Python3-BFS-Solution
# analysis: 两个list，children存储子节点们的值，nextNode存储再下次层的结点。不断更新
# recursive
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return
        def bfs(nodes):
            if not nodes:
                return
            children, nextNode = [], []
            for node in nodes:
                children.append(node.val)  # 对每一个子节点，值存入到children里
                nextNode += node.children  # 子节点存入到nextNode里
            ans.append(children)        # 把刚才得到的子节点的值们放到最后的结果list里
            bfs(nextNode)               # 进行递归
        ans.append([root.val])  # 首先把第一个存入list里面
        bfs(root.children)   # 然后把他的children放到递归函数
        # 需要注意的是不能直接把root放进去，而是要root.children开始，把之前的嫁接上去
        return ans



# source: https://leetcode.com/problems/n-ary-tree-level-order-traversal/discuss/442962/Python-99.65-100-36ms
# analysis: 使用deque来存储下一个结点们而不是list从root开始不断地更新nextNode直到，基本逻辑与上一个相同，
# 这次变成iterative

from collections import deque
class Solution_01(object):
    def levelOrder(self,root):
        if not root:
            return []
        ans = []
        nextNode = deque()
        nextNode.append(root) # 首先把第一个root存入到队列里
        while nextNode:
            children = []
            for i in range(len(nextNode)):
                node = nextNode.popleft()  # 对每一个node，值存入到children里，子节点存到nextNode里
                children.append(node.val)
                if node.children:
                    for i in node.children:
                        nextNode.append(i)
            ans.append(children)
        return ans


# 更直观易懂
class Solution_02(object):
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        level = [root]
    
        while level:
            currentNodes = []
            nextLevel = []
            for node in level:
                currentNodes.append(node.val)
                nextLevel.extend(node.children)
            res.append(currentNodes)
            level = nextLevel
        return res