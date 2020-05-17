class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

def delete_node(link, node):
    if node == link:  # 只有一个结点，头节点
        del node
    if node.next is None:  # node是尾结点
        while link:
            if link.next == node:
                link.next = None
            link = link.next
    else:
        node.val = node.next.val # 中间节点
        n_node = node.next
        node.next = n_node.next
        del n_node

def delete_node_(head,node):
    if head == node:
        del head  # 在原始的链表中删除一个节点
    if node.next is None:
        while head:
            if head.next == node:
                head.next = None
            head = head.next
    else:
        node.val = node.next.val
        temp = node.next
        node.next = temp.next
        del temp

A = ListNode(1)
A.next = ListNode(2)
A.next.next = ListNode(3)

delete_node_(A,A.next)
