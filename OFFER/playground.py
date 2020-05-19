def delete_node(head,node):
    if head == node:
        del node
    if node.next is None:
        while head:
            if head.next == node:
                head.next = None
            head = head.next
    else:
        n_node = node.next
        node.val = n_node.val
        node.next = n_node.next
        del n_node