class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        
        ROWS, COLS = len(heights), len(heights[0])
        
        pac = set()
        atl = set()
        
        def dfs(r, c, prevHeight, ocean):
          if (r < 0 or c < 0 or
              r >= ROWS or c >= COLS or
              (r,c) in ocean or 
              heights[r][c] < prevHeight):
            return
          ocean.add((r,c))
          
          dfs(r+1, c, heights[r][c], ocean)
          dfs(r-1, c, heights[r][c], ocean)
          dfs(r, c+1, heights[r][c], ocean)
          dfs(r, c-1, heights[r][c], ocean)
          
          return
          
          
        for r in range(ROWS):
          dfs(r,0,0,pac)
          dfs(r, COLS-1,0,atl)

        for c in range(COLS):
          dfs(0,c,0,pac)
          dfs(ROWS-1,c,0,atl)
          
        return pac.intersection(atl)
        
        