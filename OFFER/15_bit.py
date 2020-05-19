# 题目：二进制中1的个数
# 原来Python2的int类型有32位和64位一说，但到了Python3，当长度超过32位或64位之后，Python3会自动将其转为长整型，长整型理论上没有长度限制。
def bit_calculate(n):
    count = 0
    while n & 0xffffffff != 0: # 需要注意处理负数
        count += 1
        n = (n-1) & n  # 减去1，再与本身做与操作，就可以去掉最右边的1
    return count

def bit_(n):
    if n < 0:
        n = n & 0xffffffff # 对于负数，将最高位的符号位取反就可以获得补码，通常我们采用和0x7FFFFFFF相与来得到。
    count = 0
    while n:
        count += 1
        n = (n-1) & n
    return count
print(bit_calculate(3))
print(bit_(1))