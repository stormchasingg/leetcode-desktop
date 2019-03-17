# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead
        # 1
        pClone = pHead
        while pClone:
            node = RandomListNode(pClone.label)
            node.next = pClone.next
            pClone.next = node
            pClone = node.next
        # 2
        pClone = pHead
        while pClone:
            node = pClone.next
            if pClone.random:
                node.random = pClone.random.next
            pClone = node.next
        # 3
        pClone = pHead
        pHead = pHead.next
        while pClone.next:
            node = pClone.next
            pClone.next = node.next
            pClone = node
            
        return pHead
