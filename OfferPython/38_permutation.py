class Permutation():
    def __init__(self):
        self.temp = []
        self.ans = []
    
    def permuations(self,s):
        for i in s:
            self.temp.append(i)  # 存储去掉的这个元素，放在第一个
            new_str = s.replace(i,'') # 每次把该元素去掉，新的string进行同样的递归操作
            if len(new_str) > 0:
                self.permuations(new_str)  # 如果剩余不为空，继续递归
            else:
                self.ans.append(''.join(self.temp)) # 如果为空，代表到底了，整理到ans里面
            self.temp.pop()  # 记得将该元素pop出来，进行下一轮的选择元素
        return self.ans

ret = 'abc'
p = Permutation()
ret = p.permuations(ret)
print(ret)