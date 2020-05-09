# 视频讲解: https://www.youtube.com/watch?v=CWDQJGaN1gY
# 代码: https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
# other: http://wulc.me/2016/07/12/Binary%20Indexed%20Trees%20%E7%AE%80%E4%BB%8B/
# Python implementation of Binary Indexed Tree
# Returns sum of arr[0..index]. This function assumes
# that the array is preprocessed and partial sums of
# array elements are stored in BITree[].
def getsum(BITTree, i):
    s = 0  # initialize result
    i = i + 1
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)  # go to parent
    return s


def updatebit(BITTree, n, i, v):
    i += 1
    while i <= n:
        BITTree[i] += v
        i += i & (-i)  # go to next same level node


def construct(arr, n):
    BITTree = [0] * (n + 1)
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])
    return BITTree


# Driver code to test above methods
#freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
freq = [3,2,-1,6,5,4,-3,3,7,2,3]
BITTree = construct(freq, len(freq))
print(BITTree)
print("Sum of elements in arr[0..5] is " + str(getsum(BITTree, 5)))
