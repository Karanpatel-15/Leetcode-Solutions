class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        
        preReqs = {}
        
        for i in range(numCourses):
          preReqs[i] = []
          
        
        for c, p in prerequisites:
          preReqs[c].append(p)
          
        visited = set()
        order = []
          
        def dfs(c):
          if c in visited:
            return False
          
          if c not in preReqs:
            return True
          
          if preReqs[c] == []:
            order.append(c)
            preReqs.pop(c)
            return True
          
          visited.add(c)
          for i in preReqs[c]:
            if not dfs(i):
              return False

          preReqs.pop(c)
          visited.remove(c)
          order.append(c)
          return True
          
        for i in range(numCourses):
          if not dfs(i):
            return []
          
        return order