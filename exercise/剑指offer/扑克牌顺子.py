# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) == 0:
            return False
        numbers.sort()
        if numbers[0] == 0 and numbers[1] == 0 and numbers[2] == 0 and numbers[3] == 0:
            return True
        elif numbers[0] == 0 and numbers[1] == 0 and numbers[2] == 0:
            if len(set(numbers[3:])) == 2:
                return True if numbers[4] - numbers[3] < 5 else False
            else:
                return False
        elif numbers[0] == 0 and numbers[1] == 0:
            if len(set(numbers[2:])) == 3:
                return True if numbers[4] - numbers[2] < 5 else False
            else:
                return False
        elif numbers[0] == 0:
            if len(set(numbers[1:])) == 4:
                return True if numbers[4] - numbers[1] < 5 else False
            else:
                return False
        else:
            if len(set(numbers)) == 5:
                return True if numbers[4] - numbers[0] < 5 else False
            else:
                return False
