# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        lst1 = []
        lst2 = []
        for c in array:
            if c % 2 == 1:
                lst1.append(c)
            else:
                lst2.append(c)
        return lst1 + lst2
