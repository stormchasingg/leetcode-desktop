# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = dummy = ListNode(-1)
        dummy.next = head
        count = 0
        while fast.next:
            if count < n:
                count += 1
                fast = fast.next
            else:
                fast = fast.next
                slow = slow.next
        slow.next = slow.next.next
        return dummy.next
        
