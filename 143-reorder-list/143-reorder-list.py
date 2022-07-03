# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        def reverseList(head):  
          prev = None
          curr = head
          while curr:
            post = curr.next
            curr.next = prev
            prev = curr
            curr = post
          
          return prev
            
            
            
        def mergeList(l1, l2): 
          curr = l1
          while l2:
              l1 = l1.next
              curr.next = l2
              l2 = l2.next
              curr = curr.next
              curr.next = l1
              curr = curr.next
              
            
          
        slow = fast = head
        
        while fast.next and fast.next.next:
          fast = fast.next.next
          slow = slow.next
        
        l2 = reverseList(slow.next)
        slow.next = None
        mergeList(head, l2)
        
        return head
        