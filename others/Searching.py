# 1.1. 顺序查找
# best: O(1) worest: O(n) average:(n+1)/2 ----> O(n)
def Sequential_search(a,nums):
    for i in range(len(nums)):
        if a == nums[i]:
            return i
    return -1

# 免去了每次查找过后都要看是否越界
def Sequential_search2(a,nums):
    i = len(nums) - 1
    if i<1:
        return -1
    while nums[i]!=a:
        i-=1
    return i

# 2.2. 折半查找,前提有序数组 
# average: O(logn)
def binary_search(target,nums):
    left,right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[left]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# 1.3. 插值查找，在折半查找的基础上对mid的选择进行改造
# average: O(logn)
def interpolation_search(target,nums):
    left,right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left)*(target-nums[left]) // (nums[right] - nums[left])
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[left]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# 1.4. 裴波那契查找（Fibonacci Search）是利用黄金分割原理实现的查找方法





# 2.1 稠密索引
# 2.2 分块索引
# 2.3 倒排索引



# 3 Binary Search Tree
class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 3.1 Search in BST recursive (LeetCode700)
# O(h)
def SearchBST(node,target):
    if not node:
        return None
    if node.val == target:
        return node
    elif node.val < target:
        SearchBST(node.right,target)
    else:
        SearchBST(node.left,target)

# 3.2 Search in BST iterative (LeetCode700)
# O(h)
def SearchBST_iterative(node,target):
    while node:
        if node.val == target:
            return node
        elif node.val < target:
            node = node.right
        else:
            node = node.left 
    return None   

# 3.3 Add in BST (LeetCode701)
# O(h)
def InsertBST(root,val):
    if not root:
        return TreeNode(val)
    elif root.val < val:
        root.right = InsertBST(root.right,val)
    else:
        root.left = InsertBST(root.left,val)
    return root

# 3.4 Delete in BST (LeetCode450)
# O(h)
def DeleteBST(root,val):
    if not root:
        return root
    if root.val < val:
        root.right = DeleteBST(root.right,val)
    elif root.val > val:
        root.left = DeleteBST(root.left,val)
    else:
        if not root.left and not root.right:
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = DeleteBST(root.right,successor.val)
        elif root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            root = None
    return root

# 4 AVL Tree 平衡二叉树: @TODO: 实现平衡二叉树（大话数据结构354）
# 4.1 check if it is AVL(Leetcode 110): base case 是左右子树的高度相差不超过1，且左右子树同样是满足
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """ 
        if root == None:
            return True
        l = self.depth(root.left)
        r = self.depth(root.right)
        return (abs(l-r) <2) and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def depth(self,node):
        if node == None: return 0
        return max(self.depth(node.left),self.depth(node.right))+1





# nums = []
nums = [1,2,3,4,5]
a = 5
ans = Sequential_search(a,nums)
print("Sequential Search: ",ans)
ans = Sequential_search2(a,nums)
print("Sequential Search2: ",ans)
ans = binary_search(a,nums)
print("Binary Search: ",ans)
ans = interpolation_search(a,nums)
print("Interpolation Search: ",ans)