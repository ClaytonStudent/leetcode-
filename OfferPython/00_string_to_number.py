def string_to_number(S):
    if not S:
        return None
    res = 0
    for i in S:
        if i.isdigit():
            res = res*10 + int(i)
        else:
            return False
    return res

S = "123"
res = string_to_number(S)
print(res)



def string_to_number_(S):
    if not S:
        return None
    ans = 0
    for s in S:
        if s.isdigit():
            ans = ans*10 + int(s)
        else:
            return False
    return ans
    