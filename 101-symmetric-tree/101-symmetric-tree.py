# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
          return True
        
        def mirrorTree(l, r):
          
          if l == None and r == None:
            return True
          elif l == None or r == None or l.val != r.val:
            return False
          
          return mirrorTree(l.left, r.right) and mirrorTree(l.right, r.left)
        
        return mirrorTree(root.left, root.right)