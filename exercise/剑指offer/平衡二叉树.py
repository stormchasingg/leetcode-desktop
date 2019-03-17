# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if abs(self.getDepth(pRoot.left) - self.getDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
        
    def getDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.getDepth(pRoot.left) + 1
        right = self.getDepth(pRoot.right) + 1
        return max(left, right)
