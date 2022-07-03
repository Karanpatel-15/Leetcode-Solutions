# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        stack = []
        curr = root
        counter = 0
        
        while True:
          while curr:
            stack.append(curr)
            curr=curr.left
          
          counter += 1

          if counter == k:
            return stack.pop().val

          curr = stack.pop().right
        