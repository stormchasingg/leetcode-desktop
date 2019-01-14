# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return
        elif not (l1 and l2):
            return l1 or l2
        else:
            if l1.val + l2.val < 10:
                l3 = ListNode(l1.val + l2.val)
                l3.next = self.addTwoNumbers(l1.next, l2.next)
            else:
                l3 = ListNode(l1.val + l2.val - 10)
                l3.next = self.addTwoNumbers(l1.next, self.addTwoNumbers(l2.next, ListNode(1)))
        return l3
        
