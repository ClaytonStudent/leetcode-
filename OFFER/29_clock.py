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