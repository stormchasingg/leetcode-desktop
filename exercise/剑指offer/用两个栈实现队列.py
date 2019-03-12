# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.lst = []
    def push(self, node):
        # write code here
        self.lst.append(node)
    def pop(self):
        # return xx
        return self.lst.pop(0)
