class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        ROWS, COLS = len(grid), len(grid[0])
        
        visited = set()
        
        def dfs(r, c):
          if (r,c) in visited or r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
            return 0
          visited.add((r,c))
          dfs(r+1, c)
          dfs(r-1, c)
          dfs(r, c+1)
          dfs(r, c-1)
          
          return 1
        
        res = 0
        for r in range(ROWS):
          for c in range(COLS):
            result = dfs(r,c)
            res += result
                      
        return res