def cmp(a, b): # 安排一个新的规则
    return int(str(a)+str(b)) - int(str(b)+str(a))

def print_mini(nums):
    print(int(''.join([str(num) for num in sorted(nums, cmp=cmp)]))) # 以上述规则排序，组合成一个序列