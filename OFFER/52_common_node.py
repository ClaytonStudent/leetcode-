# source: https://github.com/JushuangQiao/Python-Offer/tree/master/fifth/third#%E9%9D%A2%E8%AF%95%E9%A2%9836-%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E9%80%86%E5%BA%8F%E5%AF%B9
# 先获取到两个链表的长度，然后长的链表先走多的几步，之后一起遍历
def get_first_common_node(link1, link2):
    if not link1 or not link2:
        return None
    length1 = length2 = 0
    move1, move2 = link1, link2
    while move1:  # 获取链表长度
        length1 += 1
        move1 = move1.next
    while move2:
        length2 += 1
        move2 = move2.next
    while length1 > length2:  # 长链表先走多的长度
        length1 -= 1
        link1 = link1.next
    while length2 > length1:
        length2 -= 1
        link2 = link2.next
    while link1:  # 链表一起走
        if link1 == link2:
            return link1
        link1, link2 = link1.next, link2.next
    return None


# source: https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solution/shuang-zhi-zhen-fa-lang-man-xiang-yu-by-ml-zimingm/
# analysis: 思路相同，更加triky，走到终点以后从另一个list的头开始走
class Solution:
    def getIntersectionNode(self, headA, headB):
        node1, node2 = headA, headB
        
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1
