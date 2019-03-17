# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_sum = array[0]
        res = max_sum
        for i in range(1, len(array)):
            max_sum = max(max_sum + array[i], array[i])
            res = max(res, max_sum)
        return res
