class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def constract_tree(preorder,inorder):
    if not preorder or not inorder:
        return None
    root_val = preorder[0]
    index = inorder.index(root_val)
    left = inorder[:index]
    right = inorder[index+1:]
    root = ListNode(root_val)
    root.left = constract_tree(preorder[1:len(left)+1],left)
    root.right = constract_tree(preorder[-len(right):],right)
    return root
#preorder = [1,2,4,7,3,5,6,8]
#inorder = [4,7,2,1,5,3,8,6]
#root = constract_tree(preorder,inorder)
#print(root.val)
#print(root.left.val)
#print(root.left.left.val)

def my(pre,inord):
    print(pre)
    print(inord)
    
    if not pre or not inord:
        return None
    root_val = pre[0]
    ind = inord.index(root_val)
    left = inord[:ind]
    right = inord[ind+1:]
    root = ListNode(root_val)
    root.left = my(pre[1:len(left)+1],left)
    root.right = my(pre[-len(right):],right)
    return root
preorder = [1,2,4,7,3,5,6,8]
inorder = [4,7,2,1,5,3,8,6]
root = my(preorder,inorder)
print(root.val)
print(root.left.val)
print(root.left.left.val)

