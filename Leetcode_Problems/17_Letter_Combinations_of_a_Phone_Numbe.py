# source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/
# analysis: backtrack 检查下一个，如果为空则把当前的组合加入到结果里，如果不为空则遍历下一个的字典值，分别加入并递归调用本函数
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for l in phone[next_digits[0]]:
                    backtrack(combination+l,next_digits[1:])
            
        output = []
        if digits:
            backtrack("", digits)
        return output

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8063/Python-solution
def letterCombinations(digits):
    dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", '8':"tuv", '9':"wxyz"}
    cmb = [''] if digits else []
    for d in digits:
        cmb = [p + q for p in cmb for q in dict[d]]
    return cmb
digits = '23'
result = letterCombinations(digits)
print('result is ',result)