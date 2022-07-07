class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        # 3 -> dead to living        
        # 4 -> living to dead
        
        ROWS, COLS = len(board), len(board[0])
        
        def checkState(x,y):
          if (x >= 0 and y >= 0 and x < ROWS and y < COLS) and (board[x][y] == 1 or board[x][y] == 4):
            return 1
          return 0
        
        def getCount(x,y):
          totalLive = 0
          directions = [[1,0],[0,1],[1,1],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1]]
          for dx, dy in directions:
            totalLive += checkState(x+dx,y+dy)
          return totalLive
          
        
        for x in range(ROWS):
          for y in range(COLS):
            count = getCount(x,y)
            state = checkState(x,y)
            print(count, state)
            if state == 1: 
              if count < 2 or count > 3:
                board[x][y] = 4           
            else:
              if count == 3:
                board[x][y] = 3
            print(board[x][y])

        for x in range(ROWS):
          for y in range(COLS):
            if board[x][y] == 3:
              board[x][y] = 1
            elif board[x][y] == 4:
              board[x][y] = 0
              