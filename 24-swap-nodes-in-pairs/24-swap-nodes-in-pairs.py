# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = prev = ListNode(0, head)
        
        while prev.next and prev.next.next:
            n1 = prev.next
            n2 = n1.next
            
            n1.next = n2.next
            n2.next = n1
            prev.next = n2
            
            prev = n1

        
        return dummy.next