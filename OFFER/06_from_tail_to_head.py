class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None
# use stack
def tail_to_head(head):
    s = []
    while head:
        s.append(head.val)
        head = head.next
    while s:
        print(s.pop())

# recurssive
def tail_to_head_(head):
    if head:
        tail_to_head(head.next)
        print(head.val)

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)

tail_to_head_(a)


def print_list(head):
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    while stack:
        print(stack.pop())
