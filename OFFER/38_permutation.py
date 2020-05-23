# combination
def my_permutation(s):
    str_set = []
    ret = []  # 最后的结果

    def permutation(string):
        for i in string:
            str_tem = string.replace(i, '')  # 每次把该元素去掉，新的string进行同样的递归操作
            str_set.append(i) # 存储去掉的这个元素，放在第一个
            if len(str_tem) > 0:
                permutation(str_tem)
            else:
                ret.append(''.join(str_set))
            str_set.pop() # 记得将该元素pop出来，进行下一轮的选择元素

    permutation(s)
    return ret




class Permutation():
    def __init__(self):
        self.temp = []
        self.ans = []
    
    def permuations(self,s):
        for i in s:
            self.temp.append(i)
            new_str = s.replace(i,'')
            if len(new_str) > 0:
                self.permuations(new_str)
            else:
                self.ans.append(''.join(self.temp))
            self.temp.pop()
        return self.ans

ret = 'abc'
p = Permutation()
ret = p.permuations(ret)
print(ret)