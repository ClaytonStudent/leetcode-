# source: https://zxi.mytechroad.com/blog/tree/leetcode-108-convert-sorted-array-to-binary-search-tree/
# analysis: BST地特性，已经排序地数组，先找最中间地元素就是根节点，然后从根节点开始，建立树，递归地建立左右子树。
# out of place vs in place: 
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/513742/Two-Python-sol.-by-divide-and-conquer.-80%2B-with-Hint-and-Comment




class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# recurssion ,in place 
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def buildBST(l,r):
            if l > r:
                return None
            m = l + (r-l) // 2
            root = TreeNode(nums[m])
            root.left = buildBST(l, m-1)
            root.right = buildBST(m+1, r)
            return root
        return buildBST(0, len(nums)-1)


# recurssion, out of place
class Solution_1(object):
    def sortedArrayToBST(self, nums):
        if len(nums) <= 0:
            return None
        # conquer
        m = len(nums) // 2
        root = TreeNode(nums[m])
        # divide
        root.left = self.sortedArrayToBST(nums[:m])
        root.right = self.sortedArrayToBST(nums[m+1:])
        return root
