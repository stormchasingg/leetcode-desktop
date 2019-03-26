# -*- coding:utf-8 -*-
import collections
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        c = collections.Counter(numbers)
        for k, v in c.items():
            if v > 1:
                duplication[0] = k
                return True
        return False
