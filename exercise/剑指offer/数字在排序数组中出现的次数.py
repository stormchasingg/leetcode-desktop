# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        key1 = 0
        key2 = 0
        l = 0
        r = 0
        for d in data:
            if d == k and key1 == 0:
                l = data.index(d)
                key1 = 1
                key2 = 1
            if key2 == 1:
                if d != k:
                    r = data.index(d)
                    break
            if key1 == 1 and d == data[-1]:
                r = len(data)
        return r-l
