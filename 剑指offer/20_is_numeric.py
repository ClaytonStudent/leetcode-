# 题目：判断输入的字符串是否满足表示数值
# -*- coding:utf-8 -*-
import re
class Solution:
    # s字符串
    def isNumeric(self, s):
        return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$", s)