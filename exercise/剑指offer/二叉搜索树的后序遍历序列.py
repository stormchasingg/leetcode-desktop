# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        i = len(sequence)-1
        for s in sequence:
            if s > sequence[-1]:
                i = sequence.index(s)
                break
        for t in sequence[i:]:
            if t < sequence[-1]:
                return False
        return i+1
