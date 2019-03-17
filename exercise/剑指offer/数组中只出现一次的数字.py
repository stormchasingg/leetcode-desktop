# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return []
        array.sort()
        res = []
        for i in range(1, len(array)-1):
            if array[i] != array[i-1] and array[i] != array[i+1]:
                res.append(array[i])
        if array[0] != array[1]:
            res.append(array[0])
        if array[-1] != array[-2]:
            res.append(array[-1])
        return res
