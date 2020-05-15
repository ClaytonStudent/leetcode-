# 使用两个hash，一个记录每个字符出现的次数，另一个记录每个字符第一次出现的位置
def first_not_repeating_char(string):
    if not string:
        return -1
    count = {}
    loc = {}
    for k, s in enumerate(string):
        count[s] = count[s] + 1 if count.get(s) else 1
        loc[s] = loc[s] if loc.get(s) else k
    ret = float('inf')
    for k in loc.keys():
        if count.get(k) == 1 and loc[k] < ret:
            ret = loc[k]
    return ret


def first_not_repeating_char_1(string):
    if not string:
        return None
    hash1, hash2 = {}, {}
    for i in range(len(string)):  # 可以用enumerate
        if string[i] not in hash1:
            hash1[string[i]] = 1  # 可以用get
            hash2[string[i]] = i
        else:
            hash1[string[i]] += 1
    min_num = float('inf')
    for i in hash2:
        if hash1[i] == 1 and hash2[i] < min_num:
            min_num = hash2[i]
    return min_num

ans = first_not_repeating_char('aabccbdd')

print(ans)

def first_not_repeating_char_2(S):
    if not S:
        return -1
    h1,h2 = {},{}
    for i,val in enumerate(S):
        h1[val] = h1[val]+ 1 if h1.get(val) else 1 # 字典不能直接用+=
        h2[val] = h2[val] if h2.get(val) else i
    min_num = float('inf')
    for i in h1.keys():
        if h1[i] == 1 and h2[i] < min_num:
            min_num = h2[i]
    return min_num

ans = first_not_repeating_char_2('aabccbdefg')
print(ans)