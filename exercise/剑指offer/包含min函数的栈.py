# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.lst = []
        
    def push(self, node):
        # write code here
        self.lst.append(node)
        
    def pop(self):
        # write code here
        return self.lst.pop()
        
    def top(self):
        # write code here
        return self.lst[::-1]
    
    def min(self):
        # write code here
        return min(self.lst)
