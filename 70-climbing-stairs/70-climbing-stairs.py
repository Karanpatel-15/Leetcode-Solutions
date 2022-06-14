class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        
        1, 2, 3, 4,
        
        1  2, 3, 5,         
        
        """
        
        one = 1
        two = 1
        
        for i in range(n-1):
          temp = one
          one = one + two
          two = temp
          
        return one