# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if not head:
          return None
        
        sizeOfList = 1
        dummy = head
        while dummy.next != None:
          dummy = dummy.next
          sizeOfList+=1
        dummy.next = head
        
        k = k % sizeOfList
        
        dummy = head
        for i in range(sizeOfList - k - 1):
          dummy = dummy.next
        
        res = dummy.next
        dummy.next = None
        
        return res
        