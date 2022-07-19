class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        
        def dfs(x, y, old):
          if (x < 0 or y < 0 or x >= len(image) or y >= len(image[0]) or image[x][y] != old):
            return 
          
          image[x][y] = color
          dfs(x+1, y, old)
          dfs(x, y+1, old)
          dfs(x, y-1, old)
          dfs(x-1, y, old)
          return 
          
          
        old = image[sr][sc]
        if old == color:
          return image
        dfs(sr,sc, old)
        return image