# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        ugly_numbers = [1] * index
        count = 1
        count2, count3, count5 = 0, 0, 0
        while count < index:
            min_value = min(ugly_numbers[count2]*2, ugly_numbers[count3]*3, ugly_numbers[count5]*5)
            ugly_numbers[count] = min_value
            while ugly_numbers[count2]*2 <= ugly_numbers[count]:
                count2 += 1
            while ugly_numbers[count3]*3 <= ugly_numbers[count]:
                count3 += 1
            while ugly_numbers[count5]*5 <= ugly_numbers[count]:
                count5 += 1
            count += 1
        return ugly_numbers[-1]
