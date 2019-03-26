# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        for num in array:
            if tsum - num in array:
                return [num, tsum-num]
        return []
