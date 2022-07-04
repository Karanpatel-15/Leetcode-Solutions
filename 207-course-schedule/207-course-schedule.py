class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        preReqs = {}
        visited = set()
        
        # populate dict
        for c, p in prerequisites:
          if c in preReqs:
            preReqs[c].append(p)
          else:
            preReqs[c] = [p]

        def dfs(i):
          
          if i in visited:
            return False
          
          if i not in preReqs:
            return True
          
          visited.add(i)
          
          for p in preReqs[i]:
            if not dfs(p):
              return False
          
          preReqs.pop(i)
          visited.remove(i)
          return True
          
        
        # go through ever course
        for i in range(numCourses):
          if not dfs(i):
            return False

        # every course preReq is completable
        return True
            
          