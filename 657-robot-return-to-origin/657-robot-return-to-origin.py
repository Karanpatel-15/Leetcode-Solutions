class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        x, y = 0, 0
        vectors = {'L':[-1,0],'R':[1,0],'U':[0,1],'D':[0,-1]}
        for m in moves:
          vector = vectors[m]
          x += vector[0]
          y += vector[1]
        
        return x == 0 and y == 0

          