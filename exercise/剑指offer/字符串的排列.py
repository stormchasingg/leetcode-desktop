# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return list(ss)
        res = []
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i] + ss[i+1:]):
                res.append(ss[i] + j)
        return sorted(set(res))
