# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def isValid(root, left, right):
          
          if not root:
            return True
          
          if left < root.val < right:
            return isValid(root.right, root.val, right) and isValid(root.left, left, root.val)
          
          return False
        
        return isValid(root, float("-inf"), float("inf"))
        