# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A or len(A) == 0:
            return []
        
        B = [1 for x in A]
        for i in range(1, len(A)):
            B[i] = B[i-1] * A[i-1]
        
        tmp = 1
        for j in range(len(A)-2, -1, -1):
            tmp *= A[j+1]
            B[j] *= tmp
        return B
