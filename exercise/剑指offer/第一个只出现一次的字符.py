# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == '':
            return -1
        for i in range(len(s)-1):
            if s[i] not in s[:i]+s[i+1:]:
                return i
        return -1
