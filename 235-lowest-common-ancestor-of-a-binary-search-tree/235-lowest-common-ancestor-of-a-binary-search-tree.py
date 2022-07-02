class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        curr = root
        
        while curr:
          if p.val > curr.val and  q.val > curr.val:
            curr = curr.right
          elif p.val < curr.val and  q.val < curr.val:
            curr = curr.left
          else: #found node or there is a split
            return curr
        