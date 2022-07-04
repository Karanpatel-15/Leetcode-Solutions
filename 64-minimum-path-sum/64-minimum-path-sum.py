class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m, n = len(grid)-1, len(grid[0])-1
        
        visited = {} 
        
        def dfs(x, y):
          
          if (x,y) in visited:
            return visited[(x,y)]
          
          s = grid[x][y]
          if(x == m and y == n):
            return s
          
          if x < m and y < n:
            s += min(dfs(x, y+1), dfs(x+1, y)) 
          elif x < m:
            s += dfs(x+1, y)
          else:
            s += dfs(x, y+1)
          
          visited[(x,y)] = s
          return s
          
        return dfs(0,0)
        
        