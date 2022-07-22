# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        
        if subRoot == None:
          return True
        if root == None:
          return False
        
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
          return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if not p and not q:
          return True
        elif not p or not q or p.val != q.val:
          return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
      