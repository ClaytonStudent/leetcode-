# 题目：定义栈的数据结构，实现找到栈的最小元素的min函数
# source:https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/solution/mian-shi-ti-30-bao-han-minhan-shu-de-zhan-fu-zhu-z/
class MinStack:
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int):
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self):
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self):
        return self.A[-1]

    def min(self):
        return self.B[-1]
