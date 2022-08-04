# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
          return
        
        
        q = [root]
        res = []
        
        while q:
          qlen = len(q)
          temp = []
          
          for i in range(qlen):
            node = q.pop(0)
            if node.left:
              q.append(node.left)
            if node.right:
              q.append(node.right)
              
            temp.append(node.val)
          res.append(temp)
          
        return res
            

        
        