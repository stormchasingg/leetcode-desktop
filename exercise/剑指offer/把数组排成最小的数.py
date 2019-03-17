# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        str_n = [str(n) for n in numbers]
        for i in range(len(str_n)-1):
            for j in range(i, len(str_n)):
                if str_n[i]+str_n[j] > str_n[j]+str_n[i]:
                    str_n[i], str_n[j] = str_n[j], str_n[i]
        return ''.join(str_n)
