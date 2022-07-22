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
          return None
        
        res = []
        queue = [root]
        
        while queue:
          qlen = len(queue)
          curr =  []
          
          for i in range(qlen):
            popped = queue.pop(0)
            if popped.left != None:
              queue.append(popped.left)
            if popped.right != None:
              queue.append(popped.right)
            curr.append(popped.val)
            
          res.append(curr)
          
        return res
        
        