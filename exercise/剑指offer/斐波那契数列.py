# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        i = 0
        a, b = 0, 1
        while i < n:
            a, b = b, a+b
            i += 1
        return a
