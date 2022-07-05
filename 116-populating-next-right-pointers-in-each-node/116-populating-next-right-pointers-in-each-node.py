# BFS Solution 
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if not root:
          return None
        
        queue = [root]
        
        while queue:
          qlen = len(queue)
          
          for i in range(qlen):
            node = queue[i]
            
            if i != qlen-1:
              node.next = queue[i+1]
              
            if node.left:
              queue.append(node.left)
            if node.right:
              queue.append(node.right)
            
          queue = queue[qlen:]
          
        return root