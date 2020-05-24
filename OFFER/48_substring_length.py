# source: https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/solution/mian-shi-ti-48-zui-chang-bu-han-zhong-fu-zi-fu-d-9/
def lengthofSubstring(s):
    dic = {}
    res = tmp = 0
    for j in range(len(s)):
        i = dic.get(s[j],-1)
        dic[s[j]] = j
        tmp = tmp +1 if tmp < j-i else j-i
        res = max(res,tmp)
    return res
