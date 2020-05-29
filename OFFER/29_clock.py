# 题目：输入一个矩阵，按照从外向里的顺序顺时针打印
def print_matrix(matrix):
    """
    :param matrix: [[]]
    """
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    start = 0
    ret = []
    while start * 2 < rows and start * 2 < cols:
        print_circle(matrix, start, rows, cols, ret)
        start += 1
    print(ret)


def print_circle(matrix, start, rows, cols, ret):
    row = rows - start - 1  # 最后一行
    col = cols - start - 1
    # left->right
    for c in range(start, col+1):
        ret.append(matrix[start][c])
    # top->bottom
    if start < row:
        for r in range(start+1, row+1):
            ret.append(matrix[r][col])
    # right->left
    if start < row and start < col:
        for c in range(start, col)[::-1]:
            ret.append(matrix[row][c])
    # bottom->top
    if start < row and start < col:
        for r in range(start+1, row)[::-1]:
            ret.append(matrix[r][start])

# source: https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/mian-shi-ti-29-shun-shi-zhen-da-yin-ju-zhen-she-di/
class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1): res.append(matrix[t][i]) # left to right
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r]) # top to bottom
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i]) # right to left
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l]) # bottom to top
            l += 1
            if l > r: break
        return res
