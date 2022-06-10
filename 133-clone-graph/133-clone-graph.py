"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        if not node:
          return node
        
        queue = [node]
        mapping = {node.val: Node(node.val, [])}
        
        while queue:
          curr = queue.pop(0)
          curr_copy = mapping[curr.val]
          for n in curr.neighbors:
            if n.val not in mapping:
              mapping[n.val] = Node(n.val, [])
              queue.append(n)
            mapping[n.val].neighbors.append(curr_copy)
        
        return mapping[node.val]
            
            
        