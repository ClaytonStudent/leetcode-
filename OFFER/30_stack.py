# 题目：定义栈的数据结构，实现找到栈的最小元素的min函数

class Stacks():
    def __init__(self):
        self.stack = []
        self.assist = []
    
    def push(self,val):
        self.stack.append(val)
        if self.assist and self.assist[-1] < val:
            self.assist.append(self.assist[-1])
        else:
            self.assist.append(val)
    
    def pop(self):
        if self.stack:
            self.assist.pop()
            return self.stack.pop()
        return None
    
    def min_(self):
        return self.assist[-1] if self.assist else None

a = Stacks()
a.push(3)
a.push(4)
a.push(2)
a.push(1)
a.pop()
a.pop()
print(a.min_())
a.push(0)
print(a.min_())