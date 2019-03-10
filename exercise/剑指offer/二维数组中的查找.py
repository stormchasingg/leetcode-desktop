# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array[0]) == 0:
            return False
        i, j = 0, len(array[0])-1
        while array[i][j] != target:
            if i == len(array)-1 or j == 0:
                return False
            if array[i][j] < target:
                i += 1
            else:
                j -= 1
        return True
#################################
size = input()
m,n = size.split()
m = int(m)
mySet = set()
for i in range(m):
    newLine = input()
    nums = newLine.split()
    for num in nums:
        mySet.add(num)
target = input() print("true") if target in mySet else print("false")
