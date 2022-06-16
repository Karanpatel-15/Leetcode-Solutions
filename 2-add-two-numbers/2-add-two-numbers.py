# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        n1, n2 = l1.val, l2.val
        l1 = l1.next
        l2 = l2.next
        
        counter = 10
        while l1:
          
          n1 += l1.val*counter
          
          counter *= 10
          l1 = l1.next
          
        counter = 10
        while l2:
          
          n2 += l2.val*counter
          
          counter *= 10
          l2 = l2.next
          
        res = n1 + n2
        dummy = curr = ListNode       
        
        while res > 9:
          curr.next = ListNode(val=res%10)
          res = res / 10 
          curr = curr.next
        curr.next = ListNode(res)
          
        return dummy.next
        