# -*- coding:utf-8 -*-
class Solution_:
    def __init__(self):
        self.count = 0
 
    def movingCount(self, threshold, rows, cols):
        # write code here
        entry = [[0 for i in range(cols)] for j in range(rows)]
        self.move(threshold, rows, cols, entry, 0, 0)
 
        return self.count
 
    def move(self, threshold, rows, cols, entry, x, y):
        if x < 0 or y < 0 or x >= rows or y >= cols:
            return
        if entry[x][y] == 1:
            return
        if x // 10 + x % 10 + y // 10 + y % 10 > threshold:
            return
        entry[x][y] = 1
        self.count += 1
        self.move(threshold, rows, cols, entry, x - 1, y)
        self.move(threshold, rows, cols, entry, x, y - 1)
        self.move(threshold, rows, cols, entry, x + 1, y)
        self.move(threshold, rows, cols, entry, x, y + 1)
S = Solution_()
num = S.movingCount(20,15,15)
print('N:',num)


def movingCount(target,rows,cols):
    nums = [[0 for i in range(cols)] for j in range(rows)]
    return move(target,rows,cols,nums,0,0)

def move(target,rows,cols,nums,x,y):
    if x <0 or y<0 or x >= rows or y >= cols:  # 越界
        return 0
    if nums[x][y] == 1: # 已经算过的
        return 0
    if x // 10 + x % 10 + y // 10 + y % 10 > target: # 超过阈值
        return 0
    nums[x][y] = 1 # 满足条件标记为1
    return 1 + move(target,rows,cols,nums,x-1,y) + move(target,rows,cols,nums,x+1,y) + move(target,rows,cols,nums,x,y-1) + move(target,rows,cols,nums,x,y+1)

print(movingCount(20,15,15))