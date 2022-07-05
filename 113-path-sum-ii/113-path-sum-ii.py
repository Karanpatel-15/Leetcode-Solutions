# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        
        res = []
        
        def dfs(root, total, currPath):
          if not root:
            return
          
          if root.val == total and not root.left and not root.right:
            currPath.append(root.val)
            res.append(currPath[:])
            return
          
          dfs(root.left, total-root.val, currPath + [root.val])
          dfs(root.right, total-root.val, currPath  + [root.val])
          return 
          
        dfs(root, targetSum, [])
        return res
          
          