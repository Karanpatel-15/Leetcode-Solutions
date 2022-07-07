class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        preReqs = {}
        
        for c, p in prerequisites:
          if c not in preReqs:
            preReqs[c] = []
          preReqs[c].append(p)
          
        visited = set()
        
        def dfs(c):
          
          if c not in preReqs or preReqs[c] == []:
            return True
          
          if c in visited:
            return False
          
          visited.add(c)
          for p in preReqs[c]:
            if not dfs(p):
              return False
          visited.remove(c)
          preReqs.pop(c)
          return True
        
        
        for i in range(numCourses):
          if not dfs(i):
            return False
        return True
          