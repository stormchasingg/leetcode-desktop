# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        numbers.sort()
        count = 1
        max_count = 1
        max_n = numbers[0]
        for i in range(len(numbers)-1):
            if numbers[i] == numbers[i+1]:
                count += 1
            else:
                count = 1
            if max_count < count:
                max_count = count
                max_n = numbers[i]
        return max_n if max_count*2 > len(numbers) else 0
