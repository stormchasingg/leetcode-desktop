# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        i = 1
        a, b = 1, 1
        while i <= number:
            a, b = b, a+b
            i += 1
        return a
