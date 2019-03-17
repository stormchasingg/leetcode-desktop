# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1, n+1):
            while i:
                if i % 10 == 1:
                    count += 1
                i /= 10
        return count
