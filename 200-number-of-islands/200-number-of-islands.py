class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        
        ROWS, COLS = len(grid), len(grid[0])
        
        res = 0
        visited = set()
        
        def dfs(r, c):
          if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0" or (r,c) in visited:
            return False
          
          visited.add((r,c))
          
          dfs(r+1,c)
          dfs(r,c+1)
          dfs(r,c-1)
          dfs(r-1,c)   
          
          return True
          
        for r in range(ROWS):
          for c in range(COLS):
            if grid[r][c] == "1":
              if dfs(r,c):
                res += 1
                
        return res

          
          
          
          
          
          
          