# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        res = ''
        for c in s:
            if c == ' ':
                res += '%20'
            else:
                res += c
        return res
