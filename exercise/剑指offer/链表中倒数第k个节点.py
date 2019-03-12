# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        res = []
        while head.next:
            res.append(head)
            head = head.next
        res.append(head)
        if k > len(res):
            return None
        return res[-k]
