# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        l, r = 1, 2
        length = (tsum + 1) / 2
        cur = l + r
        res = []
        while l < length:
            if cur == tsum:
                res.append(range(l, r+1))
            while cur > tsum and l < length:
                cur -= l
                l += 1
                if cur == tsum:
                    res.append(range(l, r+1))
            r += 1
            cur += r
        return res
