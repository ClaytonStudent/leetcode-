class Solution(object):

    @staticmethod
    def convert(tree):
        """结点转换"""
        if not tree:
            return None
        p_last = Solution.convert_nodes(tree, None)
        while p_last and p_last.left:  # 获取链表头结点
            p_last = p_last.left
        return p_last

    @staticmethod
    def convert_nodes(tree, last):
        if not tree:
            return None
        if tree.left:
            last = Solution.convert_nodes(tree.left, last)
        if last:
            last.right = tree
        tree.left = last
        last = tree
        if tree.right:
            last = Solution.convert_nodes(tree.right, last)
        return last