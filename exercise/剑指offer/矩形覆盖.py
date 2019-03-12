# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        i = 1
        a, b = 1, 1
        while i <= number:
            a, b = b, a+b
            i += 1
        return a
