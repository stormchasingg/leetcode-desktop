# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.pHead = None
        self.pTail = None
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        self.Convert(pRootOfTree.left)
        if not self.pHead:
            self.pHead = pRootOfTree
            self.pTail = pRootOfTree
        else:
            self.pTail.right = pRootOfTree
            pRootOfTree.left = self.pTail
            self.pTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.pHead
