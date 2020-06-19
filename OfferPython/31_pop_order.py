# 题目：输入两个整数序列，第一个序列表示栈的压入序列，判断第二个是不是栈的弹出序列。
class Solution:
    def validateStackSequences(self, pushed, popped):
        stack, i = [], 0
        for num in pushed:
            stack.append(num) # num 入栈
            while stack and stack[-1] == popped[i]: # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack
