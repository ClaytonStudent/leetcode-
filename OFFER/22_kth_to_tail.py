class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

def last_kth(link, k):
    if not link or k <= 0:
        return None
    move = link
    while move and k-1 >= 0: # 第一个指针移动k-n步
        move = move.next
        k -= 1
    print(k)
    while move:
        move = move.next # 第二个指针同第一个一起移动知道第一个到底
        link = link.next
    if k == 0:   #重要！这个是用来判断链表是不是比k长
        return link.val
    return None

def last_kth_(link,k):
    if not link or k <= 0:
        return None
    move = link
    while move and k>1:  # 当移动 k-1 步时，第一个指针到最后一个元素，当移动k步时候，第一个指针到None
        move = move.next
        k-=1
    while move.next:
        move = move.next
        link = link.next
    return link.val


A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(4)
E = ListNode(5)
F = ListNode(6)
A.next = B
B.next = C
C.next = D
D.next = E
E.next = F

print(last_kth(A,3))
print(last_kth_(A,3))
