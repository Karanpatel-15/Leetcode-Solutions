class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        ROWS, COLS = len(board), len(board[0])
        
        for r in range(ROWS):
          s = set()
          for c in range(COLS):
            if board[r][c] != ".": 
              if board[r][c] in s:
                return False
              else:
                s.add(board[r][c])
              
        for c in range(COLS):
          s = set()
          for r in range(ROWS):
            if board[r][c] != ".": 
              if board[r][c] in s:
                return False
              else:
                s.add(board[r][c])
        
        for rBlock in range(3):
          for cBlock in range(3):
            s = set()
            for rinner in range(3):
              for cinner in range(3):
                if board[rBlock*3+rinner][cBlock*3+cinner] != ".":
                  if board[rBlock*3+rinner][cBlock*3+cinner] in s:
                    return False
                  else:
                    s.add(board[rBlock*3+rinner][cBlock*3+cinner])
        return True