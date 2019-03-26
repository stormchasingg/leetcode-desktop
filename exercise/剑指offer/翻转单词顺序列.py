# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s == '':
            return s
        if s[0] == ' ':
            return s
        tmp = s.split()
        if len(tmp) == 1:
            return s
        else:
            for i in range(1, len(tmp)):
                tmp[i] += ' '
        return ''.join(tmp[::-1])
