# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        s = s.strip()
        if not s or len(s) < 1:
            return 0
        lookup = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        key = 0
        if len(s) == 1:
            if s in lookup.keys():
                return lookup[s]
            else:
                return 0
        if s[0] == '+':
            s = s[1:]
        if s[0] == '-':
            s = s[1:]
            key = 1
        res = 0
        for i in s:
            if i in lookup.keys():
                res = res * 10 + lookup[i]
            else:
                return 0
        return res if key == 0 else -res
